from model import *


class Controller():

    def __init__(self, rep: RepositoryABC) -> None:
        self.__rep = rep
