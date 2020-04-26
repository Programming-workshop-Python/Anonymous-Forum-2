from typing import Union

from src.app_bundle.controllers.api.abstract_api_controller import AbstractApiController
from src.app_bundle.helpers.adapters.request_entity.thread.collection.threads_adapter import ThreadsAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.thread_adapter import ThreadAdapter
from src.app_bundle.services.crud.thread_service import ThreadService


class ThreadController(AbstractApiController):
    def __init__(self, service: ThreadService, entity_adapter: Union[ThreadAdapter, None],
                 entities_adapter: Union[ThreadsAdapter, None]) -> None:
        super().__init__(service, entity_adapter, entities_adapter)
