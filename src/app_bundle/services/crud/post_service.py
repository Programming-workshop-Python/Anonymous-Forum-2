from src.app_bundle.helpers.builders.post.post_builder import PostBuilder
from src.app_bundle.repositories.post_repository import PostRepository
from src.app_bundle.services.crud.abstract_service import AbstractService
from src.app_bundle.services.validators.entity.post_validator import PostValidator


class PostService(AbstractService):

    def __init__(self, repository: PostRepository, builder: PostBuilder, validator: PostValidator) -> None:
        super().__init__(repository, builder, validator)
