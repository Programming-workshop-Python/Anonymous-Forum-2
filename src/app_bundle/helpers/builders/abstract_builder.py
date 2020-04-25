import abc
from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class AbstractBuilder:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def build(self, dto: AbstractEntityDTO) -> BaseModel:
        pass

    @abc.abstractmethod
    def rebuild(self, dto: AbstractEntityDTO, entity: BaseModel) -> BaseModel:
        pass
