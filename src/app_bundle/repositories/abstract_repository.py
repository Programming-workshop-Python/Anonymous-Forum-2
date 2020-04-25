import abc
from typing import List, Union
from src.app import App
from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.exceptions.domain_exceptions.entity.entity_not_found_exception import EntityNotFoundException


class AbstractRepository:

    __metaclass__ = abc.ABCMeta

    def __init__(self, model: BaseModel) -> None:
        self._model = model
        self._class_of_model = self._model.__class__

    def find(self, id: Union[int, str, None]) -> BaseModel:
        return App.get_db().session.query(self._class_of_model).get(id)

    def find_all(self) -> List[BaseModel]:
        return App.get_db().session.query(self._class_of_model).all()

    def get(self, id: Union[int, str, None]):
        entity = self.find(id)

        if isinstance(entity, BaseModel):
            return entity

        raise EntityNotFoundException('Entity not found')

    def save(self, entity: BaseModel):
        App.get_db().session.add(entity)

    def delete(self, entity: BaseModel) -> None:
        App.get_db().session.delete(entity)
