from src.domain.users.repositories.user_repository import UserRepository
from src.domain.users.models.user_models import CreateUserModel


def test_create_user(app):

    db = app.container.db()

    model = CreateUserModel(
        name="Vanderson Nunes",
        email="vann.nunes@gmail.com",
        password="12345678"
    )

    user_repository = UserRepository(db.session)
    user = user_repository.create_user(model)

    assert model.name == user.name
    assert model.email == user.email
    assert model.password == user.password
