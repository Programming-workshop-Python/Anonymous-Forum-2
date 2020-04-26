from typing import Union
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.app_bundle.entities.base_model import BaseModel


class Thread(BaseModel):
    __tablename__ = 'threads'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    posts = relationship('Post')

    def get_id(self) -> Union[int, str, None]:
        return self.id

    def get_name(self) -> Union[str, None]:
        return self.name

    def update_name(self, name) -> 'Thread':
        self.name = name

        return self

    def get_posts(self):
        """
        :rtype InstrumentedList[Post]
        """
        return self.posts
