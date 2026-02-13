# Base imports
# Requirements
from fastapi import FastAPI
# Support
from ..support import settings, getLogger


async def lifespan(app: FastAPI):
    yield
