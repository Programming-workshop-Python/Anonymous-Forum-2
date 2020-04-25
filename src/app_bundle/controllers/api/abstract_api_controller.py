import abc
from flask import jsonify
from src.app import App
from src.app_bundle.controllers.base_controller import BaseController


class AbstractApiController(BaseController):
    __metaclass__ = abc.ABCMeta

    def create(self, request):
        session = App.get_db().session

        try:
            entity = self._service.create(self._entity_adapter.to_dto_from_request(request))
            session.commit()
            session.flush()
            response = self._entity_adapter.to_response_data_from_entity(entity)

            return jsonify(response), 201
        except Exception as exception:
            session.rollback()
            raise exception

    def create_many(self, request):
        pass

    def update(self, request):
        session = App.get_db().session

        try:
            entity = self._service.update(self._entity_adapter.to_dto_from_request(request))
            session.commit()
            session.flush()
            response = self._entity_adapter.to_response_data_from_entity(entity)

            return jsonify(response), 200
        except Exception as exception:
            session.rollback()
            raise exception

    def update_many(self, request):
        pass

    def delete(self, request):
        session = App.get_db().session

        try:
            self._service.delete(self._entity_adapter.to_dto_from_request(request))
            session.commit()
            session.flush()

            return jsonify([]), 204
        except Exception as exception:
            session.rollback()
            raise exception

    def delete_many(self, request):
        pass

    def get_all(self):
        posts = self._service.get_all()
        response = self._entities_adapter.to_response_data_from_entities(posts)

        return jsonify(response), 200

    def get(self, request):
        entity = self._service.get(self._entity_adapter.to_dto_from_request(request))
        response = self._entity_adapter.to_response_data_from_entity(entity)

        return jsonify(response), 200
