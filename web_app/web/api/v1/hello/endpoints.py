# Base imports
from logging import Logger
# Requirements
from fastapi import FastAPI, Request


class HelloEndpoints:

    @classmethod
    async def hello(cls, request: Request) -> dict[str, str]:
        logger: Logger = request.app.state.logger
        logger.info("Hello world!")
        return {"message": "Hello world!"}
