from typing import Union

from flask import jsonify

from src.app_bundle.controllers.api.abstract_api_controller import AbstractApiController
from src.app_bundle.helpers.adapters.request_entity.thread.collection.threads_adapter import ThreadsAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.thread_adapter import ThreadAdapter
from src.app_bundle.services.crud.thread_service import ThreadService


class ThreadController(AbstractApiController):
    def __init__(self, service: ThreadService, entity_adapter: Union[ThreadAdapter, None],
                 entities_adapter: Union[ThreadsAdapter, None]) -> None:
        super().__init__(service, entity_adapter, entities_adapter)

    def get_threads_from_board(self, request):
        dto = self._entity_adapter.to_dto_from_request(request)
        entities = self._service.get_threads_from_board(dto)
        response = self._entities_adapter.to_response_data_from_entities(entities)

        return jsonify(response), 200
