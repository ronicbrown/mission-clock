# ============================================================
# Stage 1: Dependency Builder Staging
# ============================================================
FROM registry.cdso.army.mil/cdso/containers/approved-base/python_alpine:3.13 AS builder

WORKDIR /staging

# Copy dependencies manifest
COPY requirements.txt .

# Install dependencies into staging directory without root-user-action warnings
RUN python -m pip install \
    --no-cache-dir \
    --root-user-action=ignore \
    --target /install \
    -r requirements.txt

# ============================================================
# Stage 2: Final Secure Runtime Image
# ============================================================
FROM registry.cdso.army.mil/cdso/containers/approved-base/python_alpine:3.13

LABEL description="FastAPI Backend for Mission Clock"

USER root

# Clean up OS packages to mitigate CVEs
RUN apk del wget && \
    rm -rf /var/cache/apk/* /root/.cache/pip

# Create a dedicated, non-privileged system user
RUN adduser -D -h /home/app app

WORKDIR /app

# Copy dependencies and application logic from stage 1
COPY --from=builder /install /opt/dependencies
COPY main.py .

# Configure Python execution environment pathing
ENV PYTHONPATH="/opt/dependencies" \
    PYTHONDONTWRITEBYTECODE="1" \
    PYTHONUNBUFFERED="1"

# Switch to the non-root application user
USER app

EXPOSE 8000

# Start server using the dependencies paths
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
