class OrderNotFound(Exception):
    def __init__(self, message='Order tidak ditemukan!'):
        self.message = message
        super().__init__(self.message)
    pass
