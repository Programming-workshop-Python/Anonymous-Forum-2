from typing import Union
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from src.app_bundle.entities.base_model import BaseModel


class Board(BaseModel):

    __tablename__ = 'boards'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    threads = relationship('Thread')

    def get_id(self) -> Union[int, str, None]:
        return self.id

    def get_name(self) -> Union[str, None]:
        return self.name

    def update_name(self, name) -> 'Board':
        self.name = name

        return self

    def get_threads(self):
        """
        :rtype InstrumentedList[Thread]
        """
        return self.threads
