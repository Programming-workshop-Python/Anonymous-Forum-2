import abc
from typing import List

from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO
from src.app_bundle.repositories.abstract_repository import AbstractRepository
from src.app_bundle.services.validators.entity.abstract_entity_validator import AbstractEntityValidator


class AbstractService:

    __metaclass__ = abc.ABCMeta

    def __init__(self, repository: AbstractRepository, builder: AbstractBuilder, validator: AbstractEntityValidator):
        self._repository = repository
        self._builder = builder
        self._validator = validator

    def get(self, dto: AbstractEntityDTO) -> BaseModel:
        return self._repository.get(dto.get_id())

    def get_all(self) -> List[BaseModel]:
        return self._repository.find_all()

    def create(self, dto: AbstractEntityDTO) -> BaseModel:
        entity = self._builder.build(dto)
        self._validator.validate(entity)
        self._repository.save(entity)

        return entity

    def create_many(self, dto):
        pass

    def update(self, dto: AbstractEntityDTO) -> BaseModel:
        entity = self.get(dto)
        entity = self._builder.rebuild(dto, entity)
        self._validator.validate(entity)
        self._repository.save(entity)

        return entity

    def update_many(self):
        pass

    def delete(self, dto: AbstractEntityDTO):
        entity = self.get(dto)
        self._repository.delete(entity)

    def delete_many(self, dto):
        pass
