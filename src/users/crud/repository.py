from src.utils import AsyncRepository
from src.users import User


class UsersRepository(AsyncRepository):
    model = User
