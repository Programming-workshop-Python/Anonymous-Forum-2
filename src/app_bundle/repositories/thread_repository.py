from src.app_bundle.entities.thread import Thread
from src.app_bundle.repositories.abstract_repository import AbstractRepository


class ThreadRepository(AbstractRepository):
    def __init__(self, model: Thread) -> None:
        super().__init__(model)
