from typing import Union

from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class ThreadDTO(AbstractEntityDTO):

    def __init__(self, id: Union[int, None], name: Union[str, None]) -> None:
        super().__init__(id)
        self.__name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self.__name

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'name': self.get_name()
        }
