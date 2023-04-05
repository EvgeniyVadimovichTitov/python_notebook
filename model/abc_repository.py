from abc import ABC, abstractmethod
from note import*


class RepositoryABC(ABC):
    """This abc class create interface for using in process strings to Note, 
    Note to string and add new Note(BseNote to Note and save to db)"""

    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def createNewNote(self,note: BaseNote) -> None:
        pass


    @abstractmethod
    def saveListNotes(self,notes: list[Note]) -> None:
        pass


    @abstractmethod
    def getAllNotes(self)->list[Note]:
        pass
