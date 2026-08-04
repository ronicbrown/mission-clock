# Use a lightweight, official Python image to reduce vulnerabilities
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install the required Python packages (FastAPI and the Uvicorn server)
RUN pip install fastapi uvicorn

# Copy our application code (main.py) from our repo into the container
COPY main.py .

# Expose port 8000 so Kubernetes knows where to send traffic
EXPOSE 8000

# The command that runs when the container starts up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
