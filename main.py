"""
ADK Workshop - FastAPI Application 

This is the main entry point for the Cloud Run deployment.
It serves the ADK agent with a web interface for testing.
"""

import os

import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

# Configuration
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_DB_URI = "sqlite+aiosqlite:///./sessions.db"
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "*",  # Allow all origins for workshop simplicity
]
SERVE_WEB_INTERFACE = True

# Create the FastAPI application using ADK's helper
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_DB_URI,
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE,
)


@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run."""
    return {"status": "healthy", "service": "adk-workshop"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
