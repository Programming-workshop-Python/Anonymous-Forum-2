import abc
from typing import List, Dict

from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class AbstractCollectionAdapter:

    def __init__(self, entity_adapter: AbstractAdapter) -> None:
        self.__entity_adapter = entity_adapter

    @abc.abstractmethod
    def to_dto_from_request(self, request) -> List[AbstractEntityDTO]:
        pass

    @abc.abstractmethod
    def to_dto_from_list(self, request_as_list: dict) -> List[AbstractEntityDTO]:
        pass

    def to_dto_from_entities(self, entities: List[BaseModel]) -> List[AbstractEntityDTO]:
        list_with_dto = list()

        for entity in entities:
            list_with_dto.append(self.__entity_adapter.to_dto_from_entity(entity))

        return list_with_dto

    def to_response_data_from_entities(self, entities: List[BaseModel]) -> List[Dict]:
        response = []

        for entity in self.to_dto_from_entities(entities):
            response.append(entity.to_dict())

        return response
