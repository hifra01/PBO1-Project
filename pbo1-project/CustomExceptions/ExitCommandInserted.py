class ExitCommandInserted(Exception):
    def __init__(self, message='== Keluar dari program =='):
        self.message = message
        super().__init__(self.message)
    pass
