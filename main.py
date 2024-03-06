
from starlette.middleware import Middleware
from fastapi import FastAPI
from middleware.colombia_time_zone import ColombiaTimeZoneMiddleware

from app.fibonacci import fibonacci_controller

# Documentation Description for the API
description = """Backend App Proteccion"""

proteccion_app = FastAPI(
    title="Proteccion - Backend",
    description=description,
    version="0.1",
)

proteccion_app.add_middleware(ColombiaTimeZoneMiddleware)


def main():
    """
    Main function to initialize the FastAPI application.
    """
    proteccion_app.include_router(fibonacci_controller.router)


main()