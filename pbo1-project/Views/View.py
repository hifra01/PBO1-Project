import os


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
        print(f"Selamat Datang di Aplikasi Paket Wisata\n- Nikmati Pariwisata yang Komplit dan Enjoy -\n"
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
    def confirm_payment_dialog():
        View.clear_screen()
        print(":: Konfirmasi Pembayaran Pesanan ::")

    @staticmethod
    def cancel_order_dialog():
        View.clear_screen()
        print(":: Ajukan Pembatalan Order ::")

    @staticmethod
    def main_menu_dialog():
        View.clear_screen()
        print(f"Silahkan Pilih Menu Yang Ingin Dilakukan\n"
              f"1. Pesan Paket Wisata Sekarang\n"
              f"2. Riwayat Pesanan\n"
              f"3. Konfirmasi Pembayaran Pesanan\n"
              f"4. Ajukan Pembatalan Transaksi\n"
              f"Ketik 'exit' untuk keluar\n"
              f"Ketik 'back' untuk kembali ke halaman login\n\n")

    @staticmethod
    def order_history_list(orders: list):
        View.clear_screen()
        if not orders:
            print(f"Tidak ada riwayat order.\n")
        else:
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
              f"Tanggal Pulang: {detail['tanggal_pulang']}\n"
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
        View.clear_screen()
        if not paket_wisata:
            print(f"Tidak ada paket wisata.\n")
        else:
            for paket in paket_wisata:
                print(f"{paket['id']}. {paket['nama']} ({paket['durasi']} hari)")

    @staticmethod
    def admin_main_menu_dialog():
        View.clear_screen()
        print(f"Daftar Menu:\n"
              f"1. Lihat Order Menunggu Verifikasi Pembayaran\n"
              f"2. Verifikasi Pembayaran Order\n"
              f"3. Lihat Order Menunggu Pembatalan\n"
              f"4. Konfirmasi Pembatalan Order\n"
              f"5. Tambah Admin Baru\n")

    @staticmethod
    def orders_waiting_confirmation(orders: list):
        View.clear_screen()
        if not orders:
            print(f"Tidak ada riwayat order.\n")
        else:
            for order in orders:
                print(
                    f"Kode Booking: {order['kode_booking']}\n"
                    f"Customer: {order['customer']}\n"
                    f"Waktu Pesan: {order['created_date']}\n"
                    f"Status: {order['keterangan']}\n"
                )

    @staticmethod
    def verify_payment_code_dialog():
        View.clear_screen()
        print(":: Verifikasi bukti pembayaran ::")

    @staticmethod
    def verify_payment_order_detail(detail: dict):
        print(
            f"Kode Booking: {detail['kode_booking']}\n"
            f"Customer: {detail['customer']}\n"
            f"Waktu Pesan: {detail['created_date']}\n"
            f"Kode Bukti Pembayaran: {detail['kode_bukti']}\n"
            f"Status: {detail['keterangan']}\n"
        )

    @staticmethod
    def confirm_order_cancel_dialog():
        View.clear_screen()
        print(":: Konfirmasi pembatalan order ::")

    @staticmethod
    def add_new_admin_dialog():
        View.clear_screen()
        print(":: Tambah admin baru ::")
