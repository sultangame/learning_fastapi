from fastapi import APIRouter
from .posts import posts_router
from .users import admin_router


api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(posts_router)
api_v1.include_router(admin_router)
