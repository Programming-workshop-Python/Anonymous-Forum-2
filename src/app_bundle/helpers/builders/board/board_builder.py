from src.app_bundle.entities.board import Board
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.board.board_dto import BoardDTO


class BoardBuilder(AbstractBuilder):
    def build(self, dto: BoardDTO) -> Board:
        board = Board()

        board.update_name(dto.get_name())

        return board

    def rebuild(self, dto: BoardDTO, entity: Board) -> Board:
        entity.update_name(dto.get_name())

        return entity
