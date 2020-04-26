from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.board.board_dto import BoardDTO
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO
from src.app_bundle.services.crud.board_service import BoardService


class ThreadBuilder(AbstractBuilder):

    def __init__(self, board_service: BoardService) -> None:
        self._board_service = board_service
        super().__init__()

    def build(self, dto: ThreadDTO) -> Thread:
        thread = Thread()

        thread.update_name(dto.get_name()).\
            update_board(self._board_service.get(BoardDTO(dto.get_board(), dto.get_name())))

        return thread

    def rebuild(self, dto: ThreadDTO, entity: Thread) -> Thread:
        entity.update_name(dto.get_name())

        return entity
