import abc
from typing import List


class AdaptableToList:
    @abc.abstractmethod
    def to_list(self) -> List:
        pass
