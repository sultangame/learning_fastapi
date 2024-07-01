from src.utils import Service
from src.posts import Post


class PostService(Service):
    joins = [Post.owner]
    model = Post
