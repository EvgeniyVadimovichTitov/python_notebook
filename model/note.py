class BaseNote():

    """this class create for creating new note"""

    def __init__(self, head: str, body: str) -> None:
        self.__head = head
        self.__body = body

    # getter function
    @property
    def head(self) -> str:
        return self.__head

    # getter function
    @property
    def body(self) -> str:
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        self.__id = id

    # getter and setter functions for data
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    # getter and setter functions for head
    @property
    def head(self) -> str:
        return self.__head

    @head.setter
    def head(self, head: str) -> None:
        self.__head = head

    # getter and setter functions for body
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str) -> None:
        self.__body = body

    def __str__(self) -> str:
        return "id: {} data/times: {} - {:^60}\n{}\n{:^100}\n{}".format(
            self.__id, self.__data, self.__head, "-"*100, self.__body, "-"*100)
