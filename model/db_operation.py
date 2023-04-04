from abc_db_operation import *


class Operation(OperationABC):
    """This class implement OperationABC"""

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def readAllLines(super) -> list:
        with open(super._file, "r") as db:
            lines = list()
            for line in db:
                lines.append(line.rstrip())
        return lines

    def saveAllLines(super, lines: list) -> None:
        with open(super._file, "w") as db:
            for line in lines:
                db.write(line+"\n")
