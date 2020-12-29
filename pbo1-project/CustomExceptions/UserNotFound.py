class UserNotFound(Exception):
    def __init__(self, message='User tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass
