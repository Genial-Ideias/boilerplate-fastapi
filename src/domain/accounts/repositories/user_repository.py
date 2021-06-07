from src.infra.orm.entities.account import User
from src.domain.accounts.models.user_models import CreateUserModel, UserModel


class UserRepository:
    def __init__(self, db):
        self._db = db

    def create_user(self, user: CreateUserModel):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(
            email=user.email,
            password=fake_hashed_password,
            name=user.name
        )
        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        user_model = UserModel(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            is_active=db_user.is_active
        )

        return user_model
