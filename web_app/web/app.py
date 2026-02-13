# Base imports
import os
# Requirements
from fastapi import FastAPI
# Lifespan
from .lifespan import lifespan
# Support
from ..support import settings, getLogger
# Router
from .router import base_router


def application_factory():
    app_logger = getLogger("WEB_APP")
    app_logger.debug(
        f"Init WEB ASGI Application: {settings.TITLE}"
    )
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        lifespan=lifespan
    )
    app.state.logger = app_logger
    app_logger.debug(
        f"Include Router: {base_router.prefix}"
    )
    app.include_router(
        base_router
    )
    return app


def get_app_import() -> str:
    return f"{__name__}:application_factory"
