from typing import Union


class ImproveException(Exception):

    def __init__(self,
                 message: str,
                 errors: dict = {},
                 code: Union[int, str, None] = None,
                 throwable: Union[Exception, None] = None):
        self._message = message
        self._throwable = throwable
        self._errors = errors
        self._code = code

        super().__init__(message, code, throwable, errors)

    def get_message(self) -> str:
        return self._message

    def get_errors(self) -> dict:
        return self._errors

    def get_throwable(self) -> Union[Exception, None]:
        return self._throwable

    def get_code(self) -> Union[int, str, None]:
        return self._code
