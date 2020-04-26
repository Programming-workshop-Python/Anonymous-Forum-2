from src.app_bundle.helpers.builders.thread.thread_builder import ThreadBuilder
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO
from src.app_bundle.repositories.thread_repository import ThreadRepository
from src.app_bundle.services.crud.abstract_service import AbstractService
from src.app_bundle.services.validators.entity.thread_validator import ThreadValidator


class ThreadService(AbstractService):

    def __init__(self, repository: ThreadRepository, builder: ThreadBuilder, validator: ThreadValidator):
        super().__init__(repository, builder, validator)

    def get_threads_from_board(self, dto: ThreadDTO):
        return self._repository.get_threads_from_board(dto.get_board())
