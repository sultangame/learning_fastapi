from src.utils import Service
from src.users import User


class UserService(Service):
    joins = [User.posts]
    model = User
