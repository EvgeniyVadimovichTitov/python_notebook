from accessify import private

from controller.abc_controller import ControllerABC
from model.note import BaseNote
from view.enum_commands import Commands


class View():
    """This class is TUI"""

    def __init__(self, contr: ControllerABC) -> None:
        self.__contr = contr

    def ButtonClickRun(self) -> None:
        print("Welcome to NoteBook\nMENU:")
        coms = Commands
        while True:
            for com in coms:
                print("{} - {}".format(com.value, com.name))
            try:
                match int(input("Input command number: ")):
                    case coms.CREATE.value:
                        self.create()
                    case coms.SHOW_ALL.value:
                        self.showAll()
                    case coms.SHOW_EL.value:
                        self.showEl()
                    case coms.UPDATE.value:
                        self.update()
                    case coms.DEL.value:
                        self.delete()
                    case coms.SHOW_EL_BY_DATE:
                        self.showChoise()
                    case coms.EXIT.value:
                        print("Goodbye!!!")
                        break
                    case _:
                        print(
                            "Command is not found! You must replay input menu command.")
                        continue
            except Exception as err:
                print("Error:\n", err)

    @private
    def create(self) -> None:
        self.__contr.create(self.inputNote())

    @private
    def showAll(self) -> None:
        notes = self.__contr.showAll()
        if len(notes) != 0:
            for note in notes:
                print(note)
        print("Notebook is empty")

    @private
    def showEl(self) -> None:
        try:
            print(self.__contr.showNote(self.inputId()))
        except IndexError:
            print("Note is not found")

    @private
    def update(self) -> None:
        try:    
            self.__contr.update(self.inputId(), self.inputNote())
        except IndexError:
            print("Note is not found")
        

    @private
    def delete(self) -> None:
        try: 
            self.__contr.delete(self.inputId())
        except IndexError:
            print("Note is note found")

    @private
    def showChoise(self) -> None:
        notes = self.__contr.showNoteByDate(self.inputDate())
        if len(notes) != 0:
            for note in notes:
                print(note)
        else: print("Notes not found")

    @private
    def inputId(self) -> str:
        while True:
            try:
                return str(int(input("Enter Id for find: ")))
            except ValueError as err:
                print("Error:\n", err)

    @private
    def inputNote(self) -> BaseNote:
        return BaseNote(input("Header: "), input("Text: "))

    @private
    def inputDate(self) -> str:
        s = ""
        print("Enter date (format 00.00.0000): ")
        for i in ["day", "month", "year"]:
            while True:
                try:
                    buf = input("Enter {} (format is number):".format(i))
                    break
                except ValueError as err:
                    print("Error:\n", err)
            s += buf+'.'
        return s[:-1]
