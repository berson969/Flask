from typing import Type

from pydantic import BaseModel, EmailStr, ValidationError, ArbitraryTypeError
from flask_bcrypt import Bcrypt

from advs.adv import get_app
from advs.errors import ApiError

bcrypt = Bcrypt(get_app())


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str


class CreateAdvSchema(BaseModel):
    title: str
    description: str
    user_id: int


SCHEMA_TYPE = Type[CreateUserSchema] | Type[CreateAdvSchema]


def validate(data: dict, schema: SCHEMA_TYPE) -> dict:
    try:
        validated = schema(**data)
    except ValidationError as error:
        raise ApiError(400, error.errors())
    return validated.dict()


def hash_password(password: str) -> str:
    password = password.encode()
    hashed = bcrypt.generate_password_hash(password)
    return hashed.decode()


def check_password(
    password_hash: str,
    password: str,
) -> bool:
    return bcrypt.check_password_hash(password_hash.encode(), password.encode())

