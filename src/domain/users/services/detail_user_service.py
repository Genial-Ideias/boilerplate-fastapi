from src.domain.users.models.user_models import UserModel
from src.domain.users.repositories.user_repository import UserRepository


class DetailUserService:

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def detail_user(self, id: int) -> UserModel:
        users = self._detail_user(id)
        return users

    def _detail_user(self, id: int) -> UserModel:
        users = self._repository.get_by_id(id)
        return users
