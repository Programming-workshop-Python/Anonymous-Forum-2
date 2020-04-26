from typing import List, Dict

from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.adapters.request_entity.abstract_collection_adapter import AbstractCollectionAdapter
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class ThreadsAdapter(AbstractCollectionAdapter):
    def __init__(self, entity_adapter: AbstractAdapter) -> None:
        super().__init__(entity_adapter)

    def to_dto_from_request(self, request) -> List[AbstractEntityDTO]:
        pass

    def to_dto_from_list(self, request_as_list: dict) -> List[AbstractEntityDTO]:
        pass

    def to_dto_from_entities(self, entities: List[BaseModel]) -> List[AbstractEntityDTO]:
        return super().to_dto_from_entities(entities)

    def to_response_data_from_entities(self, entities: List[BaseModel]) -> List[Dict]:
        return super().to_response_data_from_entities(entities)

