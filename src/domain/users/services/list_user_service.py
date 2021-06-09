from typing import Iterator

from src.domain.users.models.user_models import UserModel
from src.domain.users.repositories.user_repository import UserRepository


class ListUserService:

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def list_users(self) -> Iterator[UserModel]:
        users = self._list_users()
        return users

    def _list_users(self) -> Iterator[UserModel]:
        users = self._repository.list_users()
        return users
