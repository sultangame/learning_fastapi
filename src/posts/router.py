from .crud import PostService, post_crud_service
from fastapi import APIRouter, Depends, status
from typing import Annotated, List
from . import models, schemas


posts_router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@posts_router.get(
    "/get/all/posts/",
    response_model=List[schemas.PostRead]
)
async def find_all_posts(
        service: Annotated[PostService, Depends(post_crud_service)]
):
    posts = await service.find_all(order_by=models.Post.title)
    return posts


@posts_router.get(
    "/get/one/{pk}/posts/",
    response_model=schemas.PostRead
)
async def find_one_posts(
        pk: int,
        service: Annotated[PostService, Depends(post_crud_service)]
):
    posts = await service.find_by_pk(pk=pk)
    return posts


@posts_router.post(
    "/add/new/post/",
    response_model=schemas.PostCreate,
    status_code=status.HTTP_201_CREATED
)
async def add_new_post(
        model: schemas.PostCreate,
        service: Annotated[PostService, Depends(post_crud_service)]
):
    answer = await service.create(schema=model)
    return answer


@posts_router.patch(
    "/edit/one/{pk}/",
    response_model=schemas.PostRead
)
async def edit_post(
        pk: int,
        model: schemas.PostUpdate,
        service: Annotated[PostService, Depends(post_crud_service)]
):
    answer = await service.edit(pk=pk, schema=model)
    return answer


@posts_router.delete("/delete/post/{pk}/")
async def delete_post(pk: int, service: Annotated[PostService, Depends(post_crud_service)]):
    answer = await service.delete(pk=pk)
    return answer
