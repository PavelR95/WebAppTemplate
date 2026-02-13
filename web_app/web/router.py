# Requirements
from fastapi import APIRouter
# Support
from ..support import settings

base_router = APIRouter(
    prefix=settings.app_base_router,
    tags=["base_router"]
)
