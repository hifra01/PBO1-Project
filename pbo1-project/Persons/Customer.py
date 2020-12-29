from .Person import Person


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


if __name__ == '__main__':
    pass
