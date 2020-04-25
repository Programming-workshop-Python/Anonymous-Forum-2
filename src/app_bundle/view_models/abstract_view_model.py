from abc import ABCMeta

from src.app_bundle.contracts.adaptable_to_dict import AdaptableToDict


class AbstractViewModel(AdaptableToDict, metaclass=ABCMeta):
    pass
