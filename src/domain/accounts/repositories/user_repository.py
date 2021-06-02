from sqlalchemy.orm import Session

from src.infra.sqlalchemy.entities.account import User
from src.domain.accounts.models.user_models import CreateUserModel


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
        self._db.refresh()
        return db_user()
