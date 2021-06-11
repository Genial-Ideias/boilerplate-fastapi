from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    password: Optional[str]


class CreateUserModel(BaseModel):
    name: str
    email: str
    password: str
