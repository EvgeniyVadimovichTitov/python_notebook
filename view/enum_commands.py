import enum

@enum.unique
class Commands(enum.Enum):
    CREATE = 1
    SHOW_ALL = 2
    SHOW_EL = 3
    UPDATE = 4
    DEL = 5
    EXIT = 0
