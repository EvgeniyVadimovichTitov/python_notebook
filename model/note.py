from accessify import private


class BaseNote():

    """this class create for creating new note"""

    def __init__(self, head: str, body: str) -> None:
        self.__head = head
        self.__body = body

    # getter function
    @property
    def get_name(self) -> str:
        return self.__head

    # getter function
    @property
    def get_body(self) -> str:
        return self.__body


class Note():
    """This class create for working with database and realithation UI"""

    def __init__(self, id: str, data: str, head: str, body: str) -> None:
        self.__id = id
        self.__data = data
        self.__head = head
        self.__body = body

    # getter and setter functions for id
    @property
    def getId(self) -> str:
        return self.__id

    @getId.setter
    def setId(self, id: str) -> None:
        self.__id = id

    # getter and setter functions for data
    @property
    def getData(self) -> str:
        return self.__data

    @getData.setter
    def setData(self, data: str) -> None:
        self.__data = data

    # getter and setter functions for head
    @property
    def getHead(self) -> str:
        return self.__head

    @getId.setter
    def setHead(self, head: str) -> None:
        self.__head = head

    # getter and setter functions for body
    @property
    def getBody(self) -> str:
        return self.__body

    @getId.setter
    def setBody(self, body: str) -> None:
        self.__body = body

    def __str__(self) -> str:
        return "id: {} data/times: {} - {:^60}\n{}\n{:^100}\n{}".format(
            self.__id, self.__data, self.__head, "-"*100, self.__body, "-"*100)
