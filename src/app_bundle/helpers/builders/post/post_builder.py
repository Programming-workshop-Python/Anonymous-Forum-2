from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.entities.post import Post
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.post.post_dto import PostDTO


class PostBuilder(AbstractBuilder):

    def build(self, dto: PostDTO) -> BaseModel:
        post = Post()

        post.update_name(dto.get_name())\
            .update_content(dto.get_content())

        return post

    def rebuild(self, dto: PostDTO, entity: Post) -> Post:
        entity.update_name(dto.get_name()).\
            update_content(dto.get_content())

        return entity

