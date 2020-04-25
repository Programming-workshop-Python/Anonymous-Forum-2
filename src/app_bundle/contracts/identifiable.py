import abc
from typing import Union


class Identifiable:

    @abc.abstractmethod
    def get_id(self) -> Union[int, str, None]:
        pass
