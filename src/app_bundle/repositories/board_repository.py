from src.app_bundle.entities.board import Board
from src.app_bundle.repositories.abstract_repository import AbstractRepository


class BoardRepository(AbstractRepository):
    def __init__(self, model: Board) -> None:
        super().__init__(model)
