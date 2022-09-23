"""File containing all the custom exceptions."""

from .m_token import Token


class MotorwayBaseError(Exception):
    """Base class for all Motorway errors to inherit from."""

    def __init__(self, token: Token, message: str):
        super().__init__(message)
        self._token = token

    @property
    def message(self):
        return str(self)

    @property
    def token(self):
        return self._token


class EmptyStackError(MotorwayBaseError):
    """Invalid modification to empty stack."""


class ParseError(MotorwayBaseError):
    """Error emitted by the parser."""
