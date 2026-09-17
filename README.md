



ronicbrown@CAZVW0FVAA3-59K:~/message-board/app/.gitlab/expedition-0/prod$ cd ~/message-board/app

echo "===== BACKEND DOCKERFILE ====="
cat backend/Dockerfile

echo
echo "===== PROD DJANGO SETTINGS ====="
cat backend/message-board/settings/prod/postgres_flexible_server.py

echo
echo "===== FRONTEND DOCKERFILE ====="
cat frontend/Dockerfile

echo
echo "===== FRONTEND DEFAULT.CONF ====="
cat frontend/default.conf

echo
echo "===== FRONTEND NGINX.CONF ====="
cat frontend/nginx.conf
===== BACKEND DOCKERFILE =====
# Dockerfile metadata for first build.
FROM registry.cdso.army.mil/cdso/containers/approved-base/python_alpine:3.14
LABEL image.authors="Caleb Sannes, @GoldenEagle"

# Create a non-root user.
RUN adduser -D message-board -h /home/message-board

# Set the working directory.
WORKDIR /home/message-board

# Install Python dependencies.
RUN apk update && \
    apk add --upgrade --no-cache libcrypto3 libssl3 && \
    apk add --no-cache --virtual=build \
    apache-arrow-dev \
    build-base \
    cmake \
    gcc \
    gcompat \
    libc-dev \
    linux-headers \
    sqlite-libs \
    xz-libs \
    --repository=https://dl-cdn.alpinelinux.org/alpine/edge/main


# Install Project requirements.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt uvicorn[standard] --break-system-packages --no-cache-dir

# Copy the source code.
COPY message-board message-board
COPY demo demo
COPY middleware middleware
COPY templates templates
COPY manage.py manage.py

# Clean-up and set permissions.
RUN apk del build &&\
    chown -R message-board:message-board /home/message-board

# Switch to the non-root user.
USER message-board

# Expose the port.
EXPOSE 8000

# Start the container.
CMD [ "python3", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "message-board.asgi:application" ]
===== PROD DJANGO SETTINGS =====
"""
Settings specific to deploying this template in AI2C's Expedition 0 using a PostgreSQL Flexible Server
"""

import os

from ..base import *

DEBUG = True

ALLOWED_HOSTS = ["ai.army.mil"]

# Ensure you add a SECRET_KEY value to the environment of the deployed container!
SECRET_KEY = os.environ["SECRET_KEY"]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASS"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}

===== FRONTEND DOCKERFILE =====
FROM registry.cdso.army.mil/cdso/containers/approved-base/node_alpine:24 AS stage_1
ENV VITE_BACKEND_URL="http://backend:8000"
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /home/message-board/
COPY message-board/ .
RUN echo "[*] VITE_BACKEND_URL has been set to '$VITE_BACKEND_URL'" &&\
    npm install &&\
    npm run build &&\
    mv "$(find dist/assets/index-*.js | head -n 1)" dist/assets/index.js

FROM registry.cdso.army.mil/cdso/containers/approved-base/alpine:3.23
LABEL image.authors="Victor Fernandez III, @cyberphor"
WORKDIR /var/lib/nginx/
RUN apk add --no-cache nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=stage_1 /home/message-board/dist/assets/ html/

EXPOSE 5173
USER nginx
CMD ["nginx", "-g", "daemon off;"]

===== FRONTEND DEFAULT.CONF =====
# /etc/nginx/conf.d/default.conf

server {
    listen 5173 default_server;

    # index.html is served as a Django template by the backend.
    location / {
        proxy_pass http://backend:8000;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Nginx will only serve index.js (the bundle created by Vite during build-time).
    location /static/ {
        alias /var/lib/nginx/html/;
    }

    access_log /dev/stdout;
    error_log /dev/stderr;
}

===== FRONTEND NGINX.CONF =====
# /etc/nginx/nginx.conf

# Set the path to store the process ID of the main nginx process.
pid logs/nginx.pid;

# Set number of worker processes automatically based on number of CPU cores.
worker_processes auto;

# Enables the use of JIT for regular expressions to speed-up their processing.
pcre_jit on;

# Sets the path and configuration for the error log.
error_log logs/error.log warn;

# Includes files with directives to load dynamic modules.
include /etc/nginx/modules/*.conf;

events {
        # The maximum number of simultaneous connections that can be opened by
        # a worker process.
        worker_connections 1024;
}

http {
        # Includes mapping of file name extensions to MIME types of responses
        # and defines the default type.
        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        # Name servers used to resolve names of upstream servers into addresses.
        # It's also needed when using tcpsocket and udpsocket in Lua modules.
        #resolver 1.1.1.1 1.0.0.1 2606:4700:4700::1111 2606:4700:4700::1001;

        # Don't tell nginx version to the clients. Default is 'on'.
        server_tokens off;

        # Specifies the maximum accepted body size of a client request, as
        # indicated by the request header Content-Length. If the stated content
        # length is greater than this size, then the client receives the HTTP
        # error code 413. Set to 0 to disable. Default is '1m'.
        client_max_body_size 1m;

        # Sendfile copies data between one FD and other from within the kernel,
        # which is more efficient than read() + write(). Default is off.
        sendfile on;

        # Causes nginx to attempt to send its HTTP response head in one packet,
        # instead of using partial frames. Default is 'off'.
        tcp_nopush on;

        # Enables the specified protocols. Default is TLSv1 TLSv1.1 TLSv1.2.
        # TIP: If you're not obligated to support ancient clients, remove TLSv1.1.
        ssl_protocols TLSv1.3;

        # Path of the file with Diffie-Hellman parameters for EDH ciphers.
        # TIP: Generate with: `openssl dhparam -out /etc/ssl/nginx/dh2048.pem 2048`
        #ssl_dhparam /etc/ssl/nginx/dh2048.pem;

        # Specifies that our cipher suits should be preferred over client ciphers.
        # Default is 'off'.
        ssl_prefer_server_ciphers on;

        # Enables a shared SSL cache with size that can hold around 8000 sessions.
        # Default is 'none'.
        ssl_session_cache shared:SSL:2m;

        # Specifies a time during which a client may reuse the session parameters.
        # Default is '5m'.
        ssl_session_timeout 1h;

        # Disable TLS session tickets (they are insecure). Default is 'on'.
        ssl_session_tickets off;

        # Enable gzipping of responses.
        #gzip on;

        # Set the Vary HTTP header as defined in the RFC 2616. Default is 'off'.
        gzip_vary on;

        # Helper variable for proxying websockets.
        map $http_upgrade $connection_upgrade {
                default upgrade;
                '' close;
        }

        # Specifies the main log format.
        log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

        # Sets the path and configuration for the access log.
        access_log logs/access.log main;

        # Includes virtual hosts configs.
        include /etc/nginx/conf.d/*.conf;

        # cDSO added security options
        etag off;

       # Directory for storing temporary files relating to client requests bodies.
        client_body_temp_path tmp/client_body;

        # Directory for storing temporary files relating to proxy requests.
        proxy_temp_path tmp/proxy;

        # Directory for storing temporary files relating to SCGI requests.
        scgi_temp_path tmp/scgi;

        # Directory for storing temporary files relating to uWSGI requests.
        uwsgi_temp_path tmp/uwsgi;

        # Directory for storing temporary files relating to FastCGI requests.
        fastcgi_temp_path tmp/fastcgi;
}
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app$
