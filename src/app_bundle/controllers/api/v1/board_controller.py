from typing import Union

from src.app_bundle.controllers.api.abstract_api_controller import AbstractApiController
from src.app_bundle.helpers.adapters.request_entity.board.board_adapter import BoardAdapter
from src.app_bundle.helpers.adapters.request_entity.board.collection.boards_adapter import BoardsAdapter
from src.app_bundle.services.crud.board_service import BoardService


class BoardController(AbstractApiController):
    def __init__(self, service: BoardService, entity_adapter: Union[BoardAdapter, None],
                 entities_adapter: Union[BoardsAdapter, None]) -> None:
        super().__init__(service, entity_adapter, entities_adapter)
