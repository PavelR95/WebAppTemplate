# Base imports
import os
# Requirements
from fastapi import FastAPI
# Lifespan
from .lifespan import lifespan
# Support
from ..support import settings, getLogger


def application_factory():
    app_logger = getLogger("WEB_APP")
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        lifespan=lifespan
    )
    return app


def get_app_import() -> str:
    return f"{__name__}:application_factory"
