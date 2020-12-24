from datetime import date, timedelta


class Order:
    def __init__(self):
        self.kode_booking: str = ""
        self.customer_id: int = int()
        self.nama_customer: str = ""
        self.id_paket_wisata: int = int()
        self.paket_wisata: str = ""
        self.id_status_order: int = int()
        self.status_order: str = ""
        self.daftar_tempat_wisata: list = list()
        self.daftar_peserta: list = list()
        self.durasi: int = int()
        self.tanggal_berangkat: date = date.today()
        self.tanggal_pulang: date = date.today()

    def set_paket_wisata(self, data: dict):
        self.id_paket_wisata = data['id']
        self.paket_wisata = data['nama']
        self.durasi = int(data['durasi'])

    def set_tanggal_berangkat(self, tanggal_berangkat: str):
        self.tanggal_berangkat = date.fromisoformat(tanggal_berangkat)
        self.tanggal_pulang = self.tanggal_berangkat + timedelta(days=self.durasi)

    def set_daftar_peserta(self, daftar_peserta):
        self.daftar_peserta = daftar_peserta
