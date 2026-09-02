FROM registry.cdso.army.mil/cdso/containers/approved-base/node_alpine:24 AS stage_1
ENV VITE_BACKEND_URL="http://backend:8000"
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /home/mission-clock/
COPY mission-clock/ .
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
COPY --from=stage_1 /home/mission-clock/dist/assets/ html/

EXPOSE 5173
USER nginx
CMD ["nginx", "-g", "daemon off;"]
