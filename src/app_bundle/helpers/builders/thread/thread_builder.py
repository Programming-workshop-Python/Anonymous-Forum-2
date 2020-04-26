from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.builders.abstract_builder import AbstractBuilder
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO


class ThreadBuilder(AbstractBuilder):
    def build(self, dto: ThreadDTO) -> Thread:
        thread = Thread()

        thread.update_name(dto.get_name())

        return thread

    def rebuild(self, dto: ThreadDTO, entity: Thread) -> Thread:
        entity.update_name(dto.get_name())

        return entity
