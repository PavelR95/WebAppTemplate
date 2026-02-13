# Base imports
# Requirements
from fastapi import FastAPI


def application_factory():
    app = FastAPI()
    return app
