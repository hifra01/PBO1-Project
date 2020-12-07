from person import Customer, Admin


class CustomerView:
    """
    Class untuk interface Customer.
    Setiap menu jadi sebuah metode tersendiri
    """

    def __init__(self):
        self.__customer = Customer()

    def start(self):
        print(f"1. Login\n"
              f"2. Register\n"
              f"0. Keluar\n\n")
        choice = input("Masukkan pilihan [0/1/2]: ")

        if choice == '1':
            self.login_dialog()
        elif choice == '2':
            self.register_dialog()

    def login_dialog(self):
        email = input("Masukkan E-mail")
        password = input("Masukkan Password")
        self.__customer.login(email, password)
        pass

    def register_dialog(self):
        # TODO: Bikin dialog pendaftaran user
        pass


class AdminView:
    """
    Class untuk interface Admin.
    Setiap menu jadi sebuah metode tersendiri
    """

    def __init__(self):
        self.__admin = Admin()

    def login_dialog(self):
        email = input("Masukkan E-mail")
        password = input("Masukkan Password")
        self.__admin.login(email, password)
        pass
