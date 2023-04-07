from enum import IntEnum, unique


@unique
class Commands(IntEnum):
    CREATE = 1
    SHOW_ALL = 2
    SHOW_EL = 3
    UPDATE = 4
    DEL = 5
    SHOW_EL_BY_DATE = 6
    EXIT = 0
