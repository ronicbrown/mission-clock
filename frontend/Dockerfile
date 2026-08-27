# ============================================================
# Use the custom CDSO Nginx base image found in the base-registry
# ============================================================
FROM registry.cdso.army.mil/cdso/containers/approved-base/nginx:1.31

LABEL description="Hardened Nginx Static Web Server for Mission Clock Frontend"

# Copy the static web application HTML file into the default Nginx directory
# Note: Ensure index.html is in the same directory as this Dockerfile (under frontend/)
COPY index.html /usr/share/nginx/html/index.html

# Expose the standard unprivileged port (8080) that matches the UDS-Package port.
# If your found image defaults to port 8443, update your service/UDS package selector accordingly.
EXPOSE 8080