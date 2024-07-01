from src.utils import AsyncRepository
from src.posts import Post


class PostRepository(AsyncRepository):
    model = Post
