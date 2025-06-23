from typing import Any, Tuple


class OrganizationError(Exception):

    DEFAULT_MESSAGE = 'Organization error'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class OrganizationNotFoundError(OrganizationError):
    DEFAULT_MESSAGE = 'Organization not found'
