import os
# from person import Customer, Admin


class View:
    """
    Setiap menu jadi sebuah metode tersendiri
    """

    @staticmethod
    def clear_screen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    @staticmethod
    def start():
        View.clear_screen()
        print(f"Selamat Datang di Aplikasi Paket Wisata\n- Nikmati Pariwisata yang Komplit dan Enjoy\n"
              f"1. Login\n"
              f"2. Register\n"
              f"Ketik 'exit' untuk keluar dari program.")

    @staticmethod
    def login_dialog():
        View.clear_screen()
        print(":: Login ke Aplikasi ::")

    @staticmethod
    def register_dialog():
        View.clear_screen()
        print(":: Buat akun baru ::")

    @staticmethod
    def main_menu_dialog():
        View.clear_screen()
        print(f"Silahkan Pilih Menu Yang Ingin Dilakukan\n"
              f"1. Pesan Paket Wisata Sekarang\n"
              f"2. Riwayat Pesanan\n"
              f"3. Ajukan Pembatalan Transaksi\n"
              f"Ketik 'exit' untuk keluar\n\n")

    @staticmethod
    def order_history_list(orders: list):
        View.clear_screen()
        for order in orders:
            print(
                f"Kode Booking: {order['kode_booking']}\n"
                f"Paket Wisata: {order['paket_wisata']}\n"
                f"Status: {order['keterangan']}\n"
            )
        print(f"Pilih menu:\n"
              f"1. Lihat detail\n"
              f"2. Kembali\n")

    @staticmethod
    def order_detail(detail: dict):
        print(f"Kode Booking: {detail['kode_booking']}\n"
              f"Paket Wisata: {detail['paket_wisata']}\n"
              f"Tanggal Berangkat: {detail['tanggal_berangkat']}\n"
              f"Tanggal Pulang: {detail['tanggal_pulang']}"
              f"Status: {detail['status']}\n\n"
              f""
              f"Daftar Destinasi Wisata:")

        for destinasi_wisata in detail['destinasi_wisata']:
            print(f"    - {destinasi_wisata['nama_tempat']}")

        print(f"\n"
              f"Daftar Peserta Wisata:")
        for peserta_wisata in detail['peserta_wisata']:
            print(f"    - {peserta_wisata['nama_peserta']} ({peserta_wisata['no_ktp']})")

    @staticmethod
    def list_paket_wisata(paket_wisata):
        for paket in paket_wisata:
            print(f"{paket['id']}. {paket['nama']} ({paket['durasi']} hari)")

#     def pesan_dialog(self):
#         View.clear_screen()
#         print("Lebih Mudah! Cukup Pilih Paket Wisata yang Anda Inginkan\n")
#         # Pilih Paket
#         choicePesan = input("Pilih Paketmu :")
#         self.tambahOrangPesan()
#         # kodePembayaran =  # kodePembayaran
#         # print("Silahkan Melakukan Pembayaran\n"
#               # f"Dengan Kode Pembayaran", kodePembayaran)
#         print("Menunggu Konfirmasi Pembayaran")
#         # Konfirmasi Admin
#         # kodeBooking =  # kodeBooking
#         # print("Pesanan Anda Telah berhasil\nDengan Kode Booking", kodeBooking)
#         pass
#
#     # def tambahOrangPesan(self)
#         nama = input("Masukkan Nama Lengkap")
#         noIdentitas = input("Massukan Nomor KTP")
#         self.__customer.register(nama, noIdentitas)
#
#     def riwayat_dialog(self):
#         # show riwayat transaksi
#         pass
#
#     def pembatalan_dialog(self):
#         kodeBooking = input("Silahkan Masukkan Kode Booking")
#         # Kode Booking Benar, Admin Konfirmasi
#         print("Menunggu Konfirmasi Pembatalan")
#         # Konfirmasi Admin
#         print("Transaksi Anda Berhasil Dibatalkan")
#
#
# class AdminView:
#     """
#     Class untuk interface Admin.
#     Setiap menu jadi sebuah metode tersendiri
#     """
#
#     def __init__(self):
#         self.__admin = Admin()
#
#     def login_dialog(self):
#         email = input("Masukkan E-mail")
#         password = input("Masukkan Password")
#         self.__admin.login(email, password)
#         pass
#
#     def berandaAdmin_dialog(sefl):
#         print(f"Selamat Datang, Admin\n"
#               f"1. Konfirmasi Pembayaran\n"
#               f"2. Konfirmasi Pembatalan GTransaksi\n")
#         f"0. Keluar"
#
#     choiceBerandaAdmin = int(input("Masukkan Pilihan [0/1/2]:"))
#
#     if choiceBerandaAdmin == 1:
#         # self.konfirmasiPembayaran_dialog()
#     elif choiceBerandaAdmin == 2:
#         self.konfirmasiPembatalan_dialog()
#
#
# def konfirmasiPembayaran_dialog(self):
#     # Lihat Transaksi & Pilih Transaksi
#     choiceKonfirmasiPembayaran = input("Konfirmasi Pembayaran\n1. Iya\n2. Tidak [1/2] :")
#
#
# def konfirmasiPembatalan_dialog(self):
#     # Lihat Transaksi & Pilih Transaksi
#     choiceKonfirmasiPembatalan = input("Konfirmasi Pembatalan\n1. Iya\n2. Tidak [1/2] :")
