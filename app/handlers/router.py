from fastapi import FastAPI

from app.handlers.routes import base_route


def include_routes(app: FastAPI) -> None:
    """Подключает ручки к приложению"""
    app.include_router(base_route.router)
