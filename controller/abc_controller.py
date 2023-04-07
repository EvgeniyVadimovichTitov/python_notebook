from abc import ABC, abstractmethod

from model.note import BaseNote, Note



class ControllerABC(ABC):
    """this abc clas is interfase for controller"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create(self, note: BaseNote) -> None:
        pass

    @abstractmethod
    def showNote(self, id: str, flag=True) -> Note:
        pass

    @abstractmethod
    def showNoteByDate(self, date: str, flag=False) -> list[Note]:
        pass

    @abstractmethod
    def showAll(self) -> list[Note]:
        pass

    @abstractmethod
    def update(self, id: str, new_note: BaseNote) -> None:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
