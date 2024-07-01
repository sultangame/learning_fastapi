from .repository import UsersRepository
from .service import UserService


def user_crud_service() -> UserService:
    return UserService(UsersRepository)
