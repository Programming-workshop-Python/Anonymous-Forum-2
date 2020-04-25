import abc
from typing import Union

from src.app_bundle.contracts.adaptable_to_dict import AdaptableToDict
from src.app_bundle.contracts.identifiable import Identifiable


class AbstractEntityDTO(Identifiable, AdaptableToDict):
    __metaclass__ = abc.ABCMeta

    def __init__(self, id: Union[int, str]) -> None:
        self._id = id
