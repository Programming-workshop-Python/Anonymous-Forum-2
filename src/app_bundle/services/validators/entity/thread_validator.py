from typing import Tuple

from src.app_bundle.entities.base_model import BaseModel
from src.app_bundle.services.validators.entity.abstract_entity_validator import AbstractEntityValidator


class ThreadValidator(AbstractEntityValidator):
    def validate(self, entity: BaseModel) -> Tuple[bool, dict]:
        pass
