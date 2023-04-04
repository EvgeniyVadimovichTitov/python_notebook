from mapper import *
from abc import ABC, abstractmethod


class OperationABC(ABC):
    """This abstract class defines an intarface working with database"""

    def __init__(self, file_name: str) -> None:
        super().__init__()
        self._file = file_name

    @abstractmethod
    def readAllLines() -> list:
        pass

    @abstractmethod
    def saveAllLines(lines: list)->None:
        pass
