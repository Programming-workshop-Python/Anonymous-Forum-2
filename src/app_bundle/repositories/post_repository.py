from src.app_bundle.entities.post import Post
from src.app_bundle.repositories.abstract_repository import AbstractRepository


class PostRepository(AbstractRepository):

    def __init__(self, model: Post) -> None:
        super().__init__(model)
