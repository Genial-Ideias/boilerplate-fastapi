from fastapi import FastAPI

from src.config import routes, containers


def create_app() -> FastAPI:
    container = containers.init_app()
    container.wire(modules=routes.get_routes())
    app = FastAPI()
    routes.init_app(app)
    app.container = container
    return app


app = create_app()
