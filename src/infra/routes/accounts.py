from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.config.database import SessionLocal

from src.domain.accounts.models.user_models import UserModel, CreateUserModel
from src.domain.accounts.services.create_account_service import CreateAccountService
from src.domain.accounts.repositories.user_repository import UserRepository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix='/users',
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserModel)
def create_user(user: CreateUserModel, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = CreateAccountService(repository=repository)
    return service.create(user)
