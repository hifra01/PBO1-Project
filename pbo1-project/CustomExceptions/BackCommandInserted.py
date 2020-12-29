class BackCommandInserted(Exception):
    def __init__(self, message='Kembali ke menu utama.'):
        self.message = message
        super().__init__(self.message)
    pass
