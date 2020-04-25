from typing import Union

from src.app_bundle.controllers.api.abstract_api_controller import AbstractApiController
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.adapters.request_entity.abstract_collection_adapter import AbstractCollectionAdapter
from src.app_bundle.services.crud.post_service import PostService


class PostController(AbstractApiController):

    def __init__(self, service: PostService, entity_adapter: Union[AbstractAdapter, None],
                 entities_adapter: Union[AbstractCollectionAdapter, None]) -> None:
        super().__init__(service, entity_adapter, entities_adapter)
