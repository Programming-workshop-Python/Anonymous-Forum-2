from src.app_bundle.helpers.builders.post.post_builder import PostBuilder
from src.app_bundle.helpers.dto.post.post_dto import PostDTO
from src.app_bundle.repositories.post_repository import PostRepository
from src.app_bundle.services.crud.abstract_service import AbstractService
from src.app_bundle.services.validators.entity.post_validator import PostValidator


class PostService(AbstractService):

    def __init__(self, repository: PostRepository, builder: PostBuilder, validator: PostValidator) -> None:
        super().__init__(repository, builder, validator)

    def get_posts_from_thread(self, dto: PostDTO):
        return self._repository.get_posts_from_thread(dto.get_thread())
