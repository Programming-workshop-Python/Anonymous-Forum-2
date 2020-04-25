import abc
from typing import Tuple
from src.app_bundle.entities.base_model import BaseModel


class AbstractEntityValidator:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, entity: BaseModel) -> Tuple[bool, dict]:
        pass
