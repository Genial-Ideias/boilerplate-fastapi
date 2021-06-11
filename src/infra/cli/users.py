import typer
from dependency_injector.wiring import inject, Provide

from src.config.containers import Container

from src.domain.users.repositories import UserRepository
from src.domain.users.services import CreateUserService
from src.domain.users.models import CreateUserModel

app = typer.Typer()

container = Container()

@app.command()
@inject
def create(
    name: str = typer.Option(..., prompt=True),
    email: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True),
    ):
    create_user_service = container.user_container.create_user_service()
    create_user_model = CreateUserModel(
        name=name,
        email=email,
        password=password
    )
    create_user_service.create(create_user_model)
    typer.echo('Usuário cirado com sucesso!')
