from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.config.containers import Container

from src.domain.users.models.user_models import CreateUserModel
from src.domain.users.services import (
    CreateUserService,
    ListUserService,
    DetailUserService,
)

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/')
@inject
def create_user(user: CreateUserModel, service: CreateUserService = Depends(Provide[Container.user_container.create_user_service])):
    return service.create(user)


@router.get('/')
@inject
def list_users(service: ListUserService = Depends(Provide[Container.user_container.list_user_service])):
    return service.list_users()


@router.get('/{id}')
@inject
def detail_user(id: int, service: DetailUserService = Depends(Provide[Container.user_container.detail_user_service])):
    return service.detail_user(id)
