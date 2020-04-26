from src.app_bundle.entities.board import Board
from src.app_bundle.exceptions.domain_exceptions.entity.validation.entity_validation_exception import \
    EntityValidationException
from src.app_bundle.services.validators.entity.abstract_entity_validator import AbstractEntityValidator


class BoardValidator(AbstractEntityValidator):

    def validate(self, entity: Board):
        errors = {'name': []}

        name = entity.get_name()

        if name is None:
            errors['name'].append('required')

        if isinstance(name, str) and len(name) > 255:
            errors['name'].append('Max length is 255')

        for key in list(errors):
            if not errors[key]:
                errors.pop(key)

        if bool(errors):
            raise EntityValidationException('Validation error', errors)
