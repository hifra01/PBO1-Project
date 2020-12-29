from .Person import Person


class Admin(Person):
    def __init__(self):
        super().__init__()
        self.__admin_id: int = int()

    def get_admin_id(self) -> int:
        return self.__admin_id

    def set_admin_id(self, admin_id: int) -> None:
        self.__admin_id = admin_id

    def set_admin_data(self, admin_data: dict) -> None:
        self.set_person_id(admin_data['person_id'])
        self.set_admin_id(admin_data['admin_id'])
        self.set_role(admin_data['role'])
        self.set_email(admin_data['email'])
        self.set_name(admin_data['nama'])


if __name__ == '__main__':
    pass
