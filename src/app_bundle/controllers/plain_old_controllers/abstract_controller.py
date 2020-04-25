import abc

from src.app_bundle.controllers.base_controller import BaseController


class AbstractController(BaseController):
    __metaclass__ = abc.ABCMeta

    def create(self):
        pass

    def create_many(self):
        pass

    def update(self):
        pass

    def update_many(self):
        pass

    def delete(self):
        pass

    def delete_many(self):
        pass

    def list(self):
        pass

    def get(self):
        pass
