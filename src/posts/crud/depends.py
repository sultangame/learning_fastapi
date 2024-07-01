from .repository import PostRepository
from .service import PostService


def post_crud_service() -> PostService:
    return PostService(PostRepository)
