from abc import ABCMeta
from src.app_bundle.contracts.adaptable_to_list import AdaptableToList


class AbstractCollectionViewModel(AdaptableToList, metaclass=ABCMeta):
    pass
