from typing import TypeVar
from chalicelib.logics import UserLogic

T = TypeVar('T')


class UserController:
    def __init__(self) -> None:
        self.__user = UserLogic()

    def list(self) -> list:
        return self.__user.list()

    def detail(self, args: T) -> T:
        return args
