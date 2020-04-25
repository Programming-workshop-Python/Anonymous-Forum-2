from datetime import datetime
from typing import Union
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO


class PostDTO(AbstractEntityDTO):

    def __init__(self, id: Union[int, None], name: Union[str, None], content: Union[str, None],
                 created_on: Union[datetime, None], updated_on: Union[datetime, None]) -> None:
        super().__init__(id)
        self.__name = name
        self.__content = content
        self.__updated_on = updated_on
        self.__created_on = created_on

    def get_id(self):
        return self._id

    def get_name(self):
        return self.__name

    def get_content(self):
        return self.__content

    def get_created_on(self):
        return self.__created_on

    def get_updated_on(self):
        return self.__updated_on

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'content': self.get_content(),
            'created_on': self.get_created_on(),
            'updated_on': self.get_updated_on(),
        }
