from typing import Union
from flask import jsonify
from src.app_bundle.controllers.api.abstract_api_controller import AbstractApiController
from src.app_bundle.helpers.adapters.request_entity.post.collection.posts_adapter import PostsAdapter
from src.app_bundle.helpers.adapters.request_entity.post.post_adapter import PostAdapter
from src.app_bundle.services.crud.post_service import PostService


class PostController(AbstractApiController):

    def __init__(self, service: PostService, entity_adapter: Union[PostAdapter, None],
                 entities_adapter: Union[PostsAdapter, None]) -> None:
        super().__init__(service, entity_adapter, entities_adapter)

    def get_posts_from_thread(self, request):
        dto = self._entity_adapter.to_dto_from_request(request)
        entities = self._service.get_posts_from_thread(dto)
        response = self._entities_adapter.to_response_data_from_entities(entities)

        return jsonify(response), 200
