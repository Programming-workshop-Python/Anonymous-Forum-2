from typing import List
from src.app_bundle.entities.post import Post
from src.app_bundle.entities.thread import Thread
from src.app_bundle.repositories.abstract_repository import AbstractRepository


class PostRepository(AbstractRepository):

    def __init__(self, model: Post) -> None:
        super().__init__(model)

    def get_posts_from_thread(self, thread_id: int) -> List[Post]:
        return Post.query.join(Thread)\
            .filter_by(id=thread_id)\
            .all()
