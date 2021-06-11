from tests.fixtures import get_new_user
from src.domain.users.models.user_models import CreateUserModel
from src.domain.users.repositories import UserRepository
from src.domain.users.services import (
    CreateUserService,
    DetailUserService
)

def test_create_user_service(app):

    db = app.container.db()

    create_user_model = CreateUserModel(
        name="Leonardo Freitas",
        email="leofreitas@email.com",
        password="12345678"
    )

    user_repository = UserRepository(db.session)
    create_user_service = CreateUserService(repository=user_repository)
    user_created = create_user_service.create(create_user_model)

    assert user_created.name == create_user_model.name
    assert user_created.email == create_user_model.email
    assert type(user_created.id) == int


def test_detail_user_service(test_client):

    db = test_client.app.container.db()
    session_factory = db.session
    with session_factory() as session:
        user = get_new_user(session)

        user_repository = UserRepository(db.session)
        detail_user_service = DetailUserService(repository=user_repository)
        user_founded = detail_user_service.detail_user(user.id)

        assert user_created.name == create_user_model.name
        assert user_created.email == create_user_model.email
        assert type(user_created.id) == int
