class UserNotFound(Exception):
    def __init__(self, message='User tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass


class ExitCommandInserted(Exception):
    def __init__(self, message='== Keluar dari program =='):
        self.message = message
        super().__init__(self.message)
    pass


class UnknownCommand(Exception):
    def __init__(self, message='Perintah tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass


class OrderNotFound(Exception):
    def __init__(self, message='Order tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass
