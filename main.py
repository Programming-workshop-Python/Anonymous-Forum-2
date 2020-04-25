from flask import Flask
from src.app import App
import logging
from src.app_bundle.exceptions.domain_exceptions.entity.entity_not_found_exception import EntityNotFoundException
from src.app_bundle.exceptions.domain_exceptions.entity.validation.entity_validation_exception import \
    EntityValidationException
from src.app_bundle.exceptions.domain_exceptions.improve_domain_exception import ImproveDomainException
from src.app_bundle.exceptions.domain_exceptions.security.base_security_exception import BaseSecurityException

app = Flask(__name__)

logging.basicConfig(filename='logs.log',
                    level=logging.FATAL,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.errorhandler(Exception)
def handle_error(exception):
    code = 500

    if isinstance(exception, ImproveDomainException):
        if isinstance(exception, EntityNotFoundException):
            code = 404
        elif isinstance(exception, BaseSecurityException):
            code = 403
        elif isinstance(exception, EntityValidationException):
            code = 422

        return jsonify(errors=exception.get_errors(), message=exception.get_message()), code

    if App.is_production_env():
        return jsonify(message='Unknown error'), code

    raise exception


with app.app_context():
    from src.app_bundle.routes.api import *
    from src.app_bundle.routes.web import *


def init_app(app: Flask):
    app = App(app)
    app.load_config()
    app.start()


if __name__ == "__main__":
    init_app(app)
