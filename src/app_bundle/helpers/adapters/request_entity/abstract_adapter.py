import abc
from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class AbstractAdapter:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def to_dto_from_request(self, request) -> AbstractEntityDTO:
        pass

    @abc.abstractmethod
    def to_dto_from_dict(self, request_as_dict: dict) -> AbstractEntityDTO:
        pass

    @abc.abstractmethod
    def to_dto_from_entity(self, entity: BaseModel) -> AbstractEntityDTO:
        pass

    def to_response_data_from_entity(self, entity: BaseModel) -> dict:
        return self.to_dto_from_entity(entity).to_dict()
