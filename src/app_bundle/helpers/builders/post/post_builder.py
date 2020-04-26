from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.entities.post import Post
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.post.post_dto import PostDTO
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO
from src.app_bundle.services.crud.thread_service import ThreadService


class PostBuilder(AbstractBuilder):

    def __init__(self, thread_service: ThreadService) -> None:
        self.thread_service = thread_service
        super().__init__()

    def build(self, dto: PostDTO) -> BaseModel:
        post = Post()

        return self.__change(post, dto)

    def rebuild(self, dto: PostDTO, entity: Post) -> Post:

        return self.__change(entity, dto)

    def __change(self, entity: Post, dto: PostDTO) -> Post:
        entity.update_name(dto.get_name()) \
            .update_content(dto.get_content()) \
            .update_thread(self.thread_service.get(ThreadDTO(dto.get_thread(), dto.get_name())))

        return entity
