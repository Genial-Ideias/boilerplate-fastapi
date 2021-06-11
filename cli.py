from typer import Typer

from src.config import cli, containers

def create_app() -> Typer:
    container = containers.init_app()
    app = Typer()
    cli.init_app(app)
    app.container = container
    return app

app = create_app()

if __name__ == '__main__':
    app()

