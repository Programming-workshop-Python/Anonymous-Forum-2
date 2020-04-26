from typing import Union
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.entities.board import Board


class Thread(BaseModel):
    __tablename__ = 'threads'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    board_id = Column(Integer(), ForeignKey('boards.id'))
    board = relationship('Board')
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

    def get_board(self) -> Board:
        return self.board

    def update_board(self, board: Board) -> 'Thread':
        self.board = board

        return self
