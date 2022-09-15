from typing import Final
from chalicelib.client import Dynamodb


class UserLogic:
    def __init__(self) -> None:
        self.__dynamodb = Final[Dynamodb()]
        self.__list = Final[list]

    def list(self) -> list:
        result = self.__dynamodb.get()
        return [
            {
                'user': 'name'
            }
        ]
