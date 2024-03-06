
from starlette.middleware import Middleware
from fastapi import FastAPI
from middleware.colombia_time_zone import ColombiaTimeZoneMiddleware


from app.fibonacci import fibonacci_controller

# Descripción de la documentación del API
descripcion = """Backend App Proteccion"""


proteccion_app = FastAPI(
    title="Proteccion - Backend",
    description=descripcion,
    version="0.1",
)

proteccion_app.add_middleware(ColombiaTimeZoneMiddleware)


def main():

    proteccion_app.include_router(fibonacci_controller.router)
    from app.config import variables_envs_manager

main()
