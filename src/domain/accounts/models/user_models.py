from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    password: str


class CreateUserModel(BaseModel):
    name: str
    email: str
    password: str
