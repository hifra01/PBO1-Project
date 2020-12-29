class UnknownCommand(Exception):
    def __init__(self, message='Perintah tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass
