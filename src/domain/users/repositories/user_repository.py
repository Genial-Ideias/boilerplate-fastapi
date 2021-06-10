from typing import Callable, ContextManager, Iterator
from sqlalchemy.orm import Session

from src.infra.orm.entities.user import User
from src.domain.users.models.user_models import CreateUserModel, UserModel


class UserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create_user(self, create_user_model: CreateUserModel) -> UserModel:
        with self.session_factory() as session:

            user_entity = User()
            user_entity.name = create_user_model.name
            user_entity.email = create_user_model.email
            user_entity.password = create_user_model.password

            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)

            user_model = UserModel(
                id=user_entity.id,
                name=user_entity.name,
                email=user_entity.email,
                is_active=user_entity.is_active,
                password=user_entity.password
            )

            return user_model

    def list_users(self) -> Iterator[UserModel]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, id: int) -> UserModel:
        with self.session_factory() as session:
            return session.query(User).filter(User.id == id).first()
