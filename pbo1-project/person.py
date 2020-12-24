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


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.__customer_id: int = int()
        self.__no_hp: str = str()
        self.__no_ktp: str = str()

    def get_customer_id(self) -> int:
        return self.__customer_id

    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id = customer_id

    def get_no_hp(self) -> str:
        return self.__no_hp

    def set_no_hp(self, no_hp: str) -> None:
        self.__no_hp = no_hp

    def get_no_ktp(self) -> str:
        return self.__no_ktp

    def set_no_ktp(self, no_ktp: str) -> None:
        self.__no_ktp = no_ktp

    def set_customer_data(self, customer_data: dict) -> None:
        self.set_person_id(customer_data['person_id'])
        self.set_customer_id(customer_data['customer_id'])
        self.set_role(customer_data['role'])
        self.set_email(customer_data['email'])
        self.set_name(customer_data['nama_lengkap'])
        self.set_no_hp(customer_data['no_hp'])
        self.set_no_ktp(customer_data['no_ktp'])


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
