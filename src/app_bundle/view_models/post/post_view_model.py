from src.app_bundle.entities.post import Post
from src.app_bundle.view_models.abstract_view_model import AbstractViewModel


class PostViewModel(AbstractViewModel):

    def __init__(self, entity: Post) -> None:
        self._entity = entity

    def to_dict(self) -> dict:
        return {
            'id': self._entity.get_id(),
            'name': self._entity.get_name(),
            'content': self._entity.get_content(),
            'created_on': self._entity.get_created_on(),
            'updated_on': self._entity.get_updated_on()
        }
