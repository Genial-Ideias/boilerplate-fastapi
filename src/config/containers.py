from dependency_injector import containers, providers

from src.config.env import environment
from src.config.database import Database

from src.infra.containers import UserContainer

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(
            Database, db_url=environment.get_item('DATABASE_URL') if not environment.get_item('TESTING', False) else environment.get_item('DATABASE_TEST_URL', 'sqlite:///')
        )

    user_container = providers.Container(UserContainer, db=db)


def init_app() -> Container:
    return Container()
