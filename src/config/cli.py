from typer import Typer

from src.infra.cli import users

def init_app(app: Typer):
    app.add_typer(users.app, name='users')
