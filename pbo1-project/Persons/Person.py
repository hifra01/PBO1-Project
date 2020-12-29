class Person:
    def __init__(self):
        super().__init__()
        self.__email: str = ""
        self.__person_id: int = int()
        self.__name: str = ""
        self.__role: str = ""

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_person_id(self) -> int:
        return self.__person_id

    def set_person_id(self, person_id: int) -> None:
        self.__person_id = person_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_role(self) -> str:
        return self.__role

    def set_role(self, role: str) -> None:
        self.__role = role


if __name__ == '__main__':
    pass
