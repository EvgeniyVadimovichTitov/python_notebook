from datetime import datetime

from model.abc_db_operation import OperationABC
from model.abc_repository import RepositoryABC
from model.mapper import mapString, mapNote
from model.note import Note, BaseNote


class Repository(RepositoryABC):
    """This implements interface abc class (RepositoryABC) and is used in process strings to Note,
    Note to string and add new Note(BseNote to Note and save to db).
    It processes lists"""

    def __init__(self, op: OperationABC) -> None:
        super().__init__()
        self.__op = op

    def getAllNotes(self) -> list[Note]:
        lines = self.__op.readAllLines()
        if len(lines)>0:
            notes = [mapString(line) for line in lines]
            return notes
        return []

    def saveListNotes(self, notes: list[Note]) -> None:
        buff_notes = [mapNote(note) for note in notes]
        self.__op.saveAllLines(buff_notes)

    def createNewNote(self, note: BaseNote) -> None:
        notes = self.getAllNotes()
        data = datetime.now().strftime("%d.%m.%Y/%H:%M:%S")
        id_max = 0
        if len(notes) != 0:
            for el in notes:
                id = int(el.id)
                if (id_max < id):
                    id_max = id
        id_max = str(id_max+1)
        new_note = Note(id_max, data, note.head, note.body)
        notes.append(new_note)
        self.saveListNotes(notes)
