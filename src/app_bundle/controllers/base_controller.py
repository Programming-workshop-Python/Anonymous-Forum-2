import abc
from typing import Union

from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.adapters.request_entity.abstract_collection_adapter import AbstractCollectionAdapter
from src.app_bundle.services.crud.abstract_service import AbstractService


class BaseController:
    __metaclass__ = abc.ABCMeta

    def __init__(self,
                 service: AbstractService,
                 entity_adapter: Union[AbstractAdapter, None],
                 entities_adapter: Union[AbstractCollectionAdapter, None]) -> None:
        self._entities_adapter = entities_adapter
        self._entity_adapter = entity_adapter
        self._service = service
