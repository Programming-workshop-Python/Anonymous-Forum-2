import abc


class AdaptableToDict:
    @abc.abstractmethod
    def to_dict(self) -> dict:
        pass
