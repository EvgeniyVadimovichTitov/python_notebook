from datetime import datetime
from accessify import private

from controller.abc_controller import ControllerABC
from model.abc_repository import RepositoryABC
from model.note import BaseNote, Note


class Controller(ControllerABC):
    """This class implement ControllerABC for working with model"""

    def __init__(self, rep: RepositoryABC) -> None:
        super().__init__()
        self.__rep = rep

    def create(self, note: BaseNote) -> None:
        self.__rep.createNewNote(note)

    def showNote(self, id: str) -> Note:
        notes = self.__rep.getAllNotes()
        return self.search(id, notes, True)[0]

    def showNoteByDate(self, date: str) -> list[Note]:
        notes = self.__rep.getAllNotes()
        if len(notes) != 0:
            return self.search(date, notes, False)
        return []

    def showAll(self) -> list[Note]:
        return self.__rep.getAllNotes()

    def update(self, id: str, new_note: BaseNote) -> None:
        notes = self.__rep.getAllNotes()
        note = self.search(id, notes, True)[0]
        note.head = new_note.head
        note.body = new_note.body
        note.data = datetime.now().strftime("%d.%m.%Y/%H:%M:%S")
        self.__rep.saveListNotes(notes)

    def delete(self, id: str) -> None:
        notes = self.__rep.getAllNotes()
        note = self.search(id, notes, True)[0]
        notes.remove(note)
        self.__rep.saveListNotes(notes)

    @private
    def search(self, finder: str, notes: list[Note], flag) -> list[Note]:
        if flag:
            return [note for note in notes if finder == note.id]
        else:
            return [note for note in notes if (finder == note.data.split("/")[0])]
