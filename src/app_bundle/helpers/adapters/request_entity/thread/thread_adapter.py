from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO


class ThreadAdapter(AbstractAdapter):

    def to_dto_from_request(self, request) -> ThreadDTO:
        id = request.args.get('id') if request.json is None else request.json.get('id')
        name = None if request.json is None else request.json.get('name')

        return self.to_dto_from_dict({
            'id': id,
            'name': name
        })

    def to_dto_from_dict(self, request_as_dict: dict) -> ThreadDTO:
        return ThreadDTO(
            request_as_dict.get('id'),
            request_as_dict.get('name')
        )

    def to_dto_from_entity(self, entity: Thread) -> ThreadDTO:
        return self.to_dto_from_dict({
            'id': entity.get_id(),
            'name': entity.get_name(),
        })

    def to_response_data_from_entity(self, entity: Thread) -> dict:
        return super().to_response_data_from_entity(entity)
