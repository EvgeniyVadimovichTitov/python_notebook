from abc import ABC, abstractmethod

class OperationABC(ABC):
    """This abstract class defines an intarface working with database"""

    def __init__(self, file_name: str) -> None:
        super().__init__()
        self._file = file_name

    @abstractmethod
    def readAllLines(self) -> list:
        pass

    @abstractmethod
    def saveAllLines(self, lines: list)->None:
        pass
