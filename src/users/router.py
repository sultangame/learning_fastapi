from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Response
from .crud import UserService, user_crud_service
from typing import Annotated
from . import models, schemas
from .utils import auth

admin_router = APIRouter(
    prefix="/admin/user",
    tags=["admin"]
)
user_router = APIRouter(
    prefix="/user/account",
    tags=["users"]
)


@admin_router.get(
    path="/get/all/users/",
    response_model=list[schemas.UserRead],
)
async def get_all_users(
        service: Annotated[UserService, Depends(user_crud_service)]
):
    answer = await service.find_all(order_by=models.User.username)
    return answer


@admin_router.post(
    path="/add/new/user/",
    response_model=schemas.UserBase,
    status_code=status.HTTP_201_CREATED
)
async def add_new_user(
        model: schemas.UserCreate,
        service: Annotated[UserService, Depends(user_crud_service)]
):
    answer = await service.create(schema=model)
    return answer


@user_router.post(
    path="/register/new/user/",
    response_model=schemas.UserRead,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
        model: schemas.UserCreate,
        service: Annotated[UserService, Depends(user_crud_service)]
):
    answer = await auth.register_new_user(user=model, service=service)
    return answer


@user_router.post(
    path="/login"
)
async def login_one_user(response: Response, data: OAuth2PasswordRequestForm = Depends()):
    token = await auth.login_users(data=data)
    response.set_cookie(key="bearer_token", value=token, httponly=True)


@user_router.get("/get/current/user/", response_model=schemas.UserRead)
async def find_current_user(jwt_token: Annotated[str | bytes, Depends(auth.token)]):
    answer = await auth.get_current_user(jwt_token=jwt_token)

    return answer


@user_router.get("/test")
async def test(jwt_token: Annotated[str | bytes, Depends(auth.token)]):
    return jwt_token
