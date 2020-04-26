from src.app_bundle.helpers.builders.board.board_builder import BoardBuilder
from src.app_bundle.repositories.board_repository import BoardRepository
from src.app_bundle.services.crud.abstract_service import AbstractService
from src.app_bundle.services.validators.entity.board_validator import BoardValidator


class BoardService(AbstractService):

    def __init__(self, repository: BoardRepository, builder: BoardBuilder, validator: BoardValidator):
        super().__init__(repository, builder, validator)
