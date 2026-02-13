# Requirements
from fastapi import APIRouter, Request
# Endpoints
from .endpoints import HelloEndpoints

router = APIRouter(
    prefix="/hello",
    tags=["v1"]
)


@router.get("/")
async def hello(request: Request):
    return await HelloEndpoints.hello(request)
