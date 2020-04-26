from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.adapters.request_entity.abstract_adapter import AbstractAdapter
from src.app_bundle.helpers.adapters.request_entity.board.board_adapter import BoardAdapter
from src.app_bundle.helpers.dto.thread.thread_dto import ThreadDTO


class ThreadAdapter(AbstractAdapter):

    def __init__(self, board_adapter: BoardAdapter) -> None:
        self._board_adapter = board_adapter
        super().__init__()

    def to_dto_from_request(self, request) -> ThreadDTO:
        id = request.args.get('id') if request.json is None else request.json.get('id')
        name = None if request.json is None else request.json.get('name')
        board = request.args.get('board') if request.json is None else request.json.get('board')

        return self.to_dto_from_dict({
            'id': id,
            'name': name,
            'board': board
        })

    def to_dto_from_dict(self, request_as_dict: dict) -> ThreadDTO:
        return ThreadDTO(
            request_as_dict.get('id'),
            request_as_dict.get('name'),
            request_as_dict.get('board')
        )

    def to_dto_from_entity(self, entity: Thread) -> ThreadDTO:
        return self.to_dto_from_dict({
            'id': entity.get_id(),
            'name': entity.get_name(),
            'board': self._board_adapter.to_dto_from_entity(entity.get_board()).to_dict()
        })

    def to_response_data_from_entity(self, entity: Thread) -> dict:
        return super().to_response_data_from_entity(entity)
