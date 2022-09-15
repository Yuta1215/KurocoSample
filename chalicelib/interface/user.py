import abc


class UserControllerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list(self) -> list:
        pass


class UserDataInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self) -> None:
        pass

    @abc.abstractmethod
    def update(self) -> None:
        pass

    @abc.abstractmethod
    def delete(self) -> None:
        pass
