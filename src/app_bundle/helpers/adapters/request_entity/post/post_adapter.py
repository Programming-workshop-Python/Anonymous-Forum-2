from typing import Union

from src.app_bundle.entities.post import Post
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.dto.abstract_entity_dto import AbstractEntityDTO
from src.app_bundle.helpers.dto.post.post_dto import PostDTO


class PostAdapter(AbstractAdapter):

    def to_dto_from_entity(self, entity: Post) -> Union[AbstractEntityDTO, PostDTO]:
        return self.to_dto_from_dict({
            'id': entity.get_id(),
            'name': entity.get_name(),
            'content': entity.get_content(),
            'created_on': entity.get_created_on(),
            'updated_on': entity.get_updated_on()
        })

    def to_dto_from_request(self, request):
        id = request.args.get('id') if request.json is None else request.json.get('id')
        name = None if request.json is None else request.json.get('name')
        content = None if request.json is None else request.json.get('content')

        return self.to_dto_from_dict({
            'id': id,
            'name': name,
            'content': content,
            'created_on': content,
            'updated_on': content
        })

    def to_dto_from_dict(self, request_as_dict: dict):
        return PostDTO(
            request_as_dict.get('id'),
            request_as_dict.get('name'),
            request_as_dict.get('content'),
            request_as_dict.get('created_on'),
            request_as_dict.get('updated_on'),
        )
