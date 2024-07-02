from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jwt import InvalidTokenError

from src.users import schemas, User
from .hash_password import hash_password, check_password
from sqlalchemy import select
from src.database import async_session_maker
from src.users.crud import UserService, user_crud_service
from typing import Annotated
from .jwt_token import decode_jwt, encode_jwt


token = OAuth2PasswordBearer(tokenUrl="/api/v1/user/account/login")


async def find_one_user(username):
    async with async_session_maker() as session:
        stmt = select(User).where(User.username == username)
        result = await session.execute(stmt)
        return result.scalar()


async def register_new_user(
        user: schemas.UserCreate,
        service: Annotated[UserService, Depends(user_crud_service)]
):

    user_check = await find_one_user(user.username)
    if user_check is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    hashing_password = hash_password(user.hashed_password)
    user.hashed_password = hashing_password
    new_user = await service.create(user)
    return new_user


async def login_users(data: OAuth2PasswordRequestForm = Depends()):
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="password or username is incorrect"
    )
    user = await find_one_user(username=data.username)
    if user is None:
        raise exception
    if not check_password(data.password, user.hashed_password):
        raise exception
    payload = {
        "sub": data.username,
        "email": user.email
    }
    access_token = encode_jwt(payload=payload)
    print(access_token)
    return access_token


async def get_current_user(
        jwt_token: Annotated[str | bytes, Depends(token)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt(token=jwt_token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user: User = await find_one_user(username=token_data.username)
    return user
