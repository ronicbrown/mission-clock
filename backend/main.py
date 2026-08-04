# Import FastAPI to create the web server framework
from fastapi import FastAPI
# Import datetime tools to generate the current time
from datetime import datetime, timezone

# Initialize the FastAPI application instance
app = FastAPI()

# Create a route that listens for GET requests at the "/time" URL path
@app.get("/time")
def get_time():
    # Generate the current time in UTC (Zulu time)
    # Format it as a standard ISO 8601 string (e.g., 2026-08-04T11:04:27Z)
    zulu_time_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Return the time as a JSON dictionary to the frontend
    return {"zulu_time": zulu_time_str}
