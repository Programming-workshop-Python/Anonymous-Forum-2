from typing import List
from src.app_bundle.entities.post import Post
from src.app_bundle.view_models.post.post_view_model import PostViewModel


class PostsViewModel:

    def __init__(self, posts: List[Post]) -> None:
        self._posts = posts

    def to_list(self) -> List[dict]:
        posts = []

        for post in self._posts:
            posts.append(PostViewModel(post).to_dict())

        return posts
