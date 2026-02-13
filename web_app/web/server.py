# Base imports
# Requirements
import uvicorn
# Application
from .app import application_factory


def run_server():
    app = application_factory()
    uvicorn.run(
        app=app
    )
