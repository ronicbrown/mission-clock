# CRITICAL: Use an "unprivileged" Nginx image. 
# Standard Nginx runs as 'root', which is banned by DoD IL5 security policies.
FROM nginxinc/nginx-unprivileged:alpine

# Copy our custom HTML file to the directory where Nginx serves web pages
COPY index.html /usr/share/nginx/html/index.html

# Expose port 8080 (unprivileged containers cannot use standard port 80)
EXPOSE 8080
