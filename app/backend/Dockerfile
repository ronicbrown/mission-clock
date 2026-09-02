# Dockerfile metadata for first build.
FROM registry.cdso.army.mil/cdso/containers/approved-base/python_alpine:3.14
LABEL image.authors="Caleb Sannes, @GoldenEagle"

# Create a non-root user.
RUN adduser -D mission-clock -h /home/mission-clock

# Set the working directory.
WORKDIR /home/mission-clock

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
COPY mission-clock mission-clock
COPY demo demo
COPY middleware middleware
COPY templates templates
COPY manage.py manage.py

# Clean-up and set permissions.
RUN apk del build &&\
    chown -R mission-clock:mission-clock /home/mission-clock

# Switch to the non-root user.
USER mission-clock

# Expose the port.
EXPOSE 8000

# Start the container.
CMD [ "python3", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "mission-clock.asgi:application" ]