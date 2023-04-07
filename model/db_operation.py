from pathlib import Path

from model.abc_db_operation import OperationABC



class Operation(OperationABC):
    """This class implement OperationABC"""

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)
        file = Path(file_name)
        file.touch(exist_ok=True)
        f = open(file)

    def readAllLines(self) -> list[str]:
        with open(self._file, "r") as db:
            lines = [line.rstrip() for line in db]
        return lines

    def saveAllLines(self, lines: list[str]) -> None:
        with open(self._file, "w") as db:
            for line in lines:
                db.write(line+"\n")
