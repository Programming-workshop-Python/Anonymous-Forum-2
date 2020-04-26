from typing import List, Dict
from src.app_bundle.entities.board import Board
from src.app_bundle.helpers.adapters.request_entity.abstract_collection_adapter import AbstractCollectionAdapter
from src.app_bundle.helpers.adapters.request_entity.board.board_adapter import BoardAdapter
from src.app_bundle.helpers.dto.board.board_dto import BoardDTO


class BoardsAdapter(AbstractCollectionAdapter):
    def __init__(self, entity_adapter: BoardAdapter) -> None:
        super().__init__(entity_adapter)

    def to_dto_from_request(self, request) -> List[BoardDTO]:
        pass

    def to_dto_from_list(self, request_as_list: dict) -> List[BoardDTO]:
        pass

    def to_dto_from_entities(self, entities: List[Board]) -> List[BoardDTO]:
        return super().to_dto_from_entities(entities)

    def to_response_data_from_entities(self, entities: List[Board]) -> List[Dict]:
        return super().to_response_data_from_entities(entities)

