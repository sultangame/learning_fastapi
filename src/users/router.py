from fastapi import APIRouter, Depends, status
from .crud import UserService, user_crud_service
from typing import Annotated
from . import models, schemas


admin_router = APIRouter(
    prefix="/admin/user",
    tags=["admin"]
)


@admin_router.get(
    "/get/all/users/",
    response_model=list[schemas.UserRead],
)
async def get_all_users(
        service: Annotated[UserService, Depends(user_crud_service)]
):
    answer = await service.find_all(order_by=models.User.username)
    return answer


@admin_router.post(
    "/add/new/user/",
    response_model=schemas.UserBase,
    status_code=status.HTTP_201_CREATED
)
async def add_new_user(model: schemas.UserCreate, service: Annotated[UserService, Depends(user_crud_service)]):
    answer = await service.create(schema=model)
    return answer
