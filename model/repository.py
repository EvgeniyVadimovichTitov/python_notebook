from abc_repository import *
from abc_db_operation import OperationABC
from mapper import *
import datetime


class Repository(RepositoryABC):
    """This implements interface abc class (RepositoryABC) and is used in process strings to Note,
    Note to string and add new Note(BseNote to Note and save to db).
    It processes lists"""

    def __init__(self, op: OperationABC) -> None:
        super().__init__()
        self.__op = op

    def getAllNotes(self) -> list[Note]:
        lines = self.__op.readAllLines()
        notes = [mapString(line) for line in lines]
        return notes

    def saveListNotes(self, notes: list[Note]) -> None:
        buff_notes = [mapNote(note) for note in notes]
        self.__op.saveAllLines(buff_notes)

    def createNewNote(self, note: BaseNote) -> None:
        notes = self.getAllNotes()
        data = datetime.datetime.now().strftime("%d.%m.%Y/%H:%M:%S")
        id_max = 0
        if len(notes) != 0:
            for el in notes:
                id = int(el.getId)
                if (id_max < id):
                    id_max = id
        id_max = str(id_max+1)
        new_note = Note(id_max, data, note.getHead, note.getBody)
        notes.append(new_note)
        self.saveListNotes(notes)
