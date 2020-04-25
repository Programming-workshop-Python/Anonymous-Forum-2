from typing import Union

from src.app_bundle.exceptions.domain_exceptions.improve_domain_exception import ImproveDomainException


class BaseEntityException(ImproveDomainException):

    def __init__(self,
                 message: str,
                 errors: dict = {},
                 code: Union[int, str, None] = None,
                 throwable: Union[Exception, None] = None):
        super().__init__(message, errors, code, throwable)
