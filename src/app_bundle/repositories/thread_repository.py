from typing import List
from src.app_bundle.entities.board import Board
from src.app_bundle.entities.thread import Thread
from src.app_bundle.repositories.abstract_repository import AbstractRepository


class ThreadRepository(AbstractRepository):
    def __init__(self, model: Thread) -> None:
        super().__init__(model)

    def get_threads_from_board(self, board_id: int) -> List[Thread]:
        return Thread.query.join(Board) \
            .filter_by(id=board_id) \
            .all()
