from getpass import getpass
from .BaseController import BaseController
from Persons import Customer
from Models import CustomerModel
from Views import View
from Orders import Order
import CustomExceptions as cExc


class CustomerController(BaseController):
    def __init__(self, db_config_file):
        super().__init__(db_config_file)
        self.customer: Customer = Customer()
        self._cs_model: CustomerModel = CustomerModel(db_config_file)

    def generate_kode_booking(self, order: Order):
        id_kota = self._order_model.get_city_id_from_paket_wisata(order)
        new_id = int(self._order_model.get_last_order_id()) + 1
        new_booking_code = str(id_kota) + str(order.id_paket_wisata) + str(new_id).zfill(5)
        return new_booking_code

    def start(self):
        while True:
            try:
                View.start()
                choice = input("Masukkan pilihanmu [1/2/exit]: ")
                if choice.lower() == 'exit':
                    raise cExc.ExitCommandInserted()
                elif choice == '1':
                    self.login()
                elif choice == '2':
                    self.register()
                else:
                    raise cExc.UnknownCommand('Pilihan tidak valid.')
            except cExc.UnknownCommand as e:
                print(e)
                input("Tekan Enter untuk melanjutkan")
            except cExc.ExitCommandInserted as e:
                print(e)
                break
            except KeyboardInterrupt:
                print("Force quit app.")
                break

    def login(self) -> None:
        while True:
            try:
                View.login_dialog()
                email: str = input("Masukkan email (ketik 'exit' untuk keluar atau 'back' untuk kembali): ")
                if email.lower() == 'exit':
                    raise cExc.ExitCommandInserted()
                elif email.lower() == 'back':
                    raise cExc.BackCommandInserted()
                else:
                    password: str = getpass("Masukkan password: ")
                    login = self._cs_model.login(email=email, password=password)
                    if login:
                        self.customer.set_customer_data(self._cs_model.login(email=email, password=password))
                        self.main_menu()
            except cExc.UserNotFound as e:
                print(e)
                input("Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break

    def register(self):
        while True:
            try:
                register_data = dict()
                nama_input = input("Masukkan Nama Lengkap (Ketik 'back' untuk kembali): ")
                if nama_input.lower() == 'back':
                    raise cExc.BackCommandInserted
                else:
                    register_data['nama'] = nama_input
                    register_data['no_ktp'] = input("Masukkan Nomor KTP: ")
                    register_data['no_hp'] = input("Masukkan Nomor HP: ")
                    register_data['email'] = input("Masukkan E-mail: ")

                    new_password = getpass("Masukkan Password baru: ")
                    confirm_new_password = getpass('Konfirmasi Password baru Anda: ')
                    if new_password == confirm_new_password:
                        confirm = input("Apakah Anda ingin mendaftarkan akun tersebut? [y/N]")
                        if confirm.lower() == 'y':
                            register_data['password'] = new_password
                            self._cs_model.register_new_user(register_data)
                            input('Pendaftaran Akun Baru berhasil. Tekan Enter untuk melanjutkan...')
                        else:
                            input('Pendaftaran Akun Baru dibatalkan. Tekan Enter untuk melanjutkan...')
                        break
                    else:
                        input("Password tidak sesuai! Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break

    def main_menu(self):
        while True:
            try:
                View.main_menu_dialog()
                choice = input("Masukkan Pilihan [1/2/3/4/exit]: ")
                if choice.lower() == 'exit':
                    raise cExc.ExitCommandInserted()
                elif choice.lower() == 'back':
                    raise cExc.BackCommandInserted()
                else:
                    if choice == '1':
                        self.new_order()
                    elif choice == '2':
                        self.list_order_history()
                    elif choice == '3':
                        self.confirm_payment()
                    elif choice == '4':
                        self.cancel_order()
                    else:
                        input("Pilihan tidak valid. Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break

    def new_order(self):
        new_order = Order()
        new_order.customer_id = self.customer.get_customer_id()

        while True:
            try:
                daftar_paket_wisata = self._order_model.get_daftar_paket_wisata()
                View.list_paket_wisata(daftar_paket_wisata)
                paket_wisata_choice = input("Masukkan nomor paket wisata (ketik 'back' untuk kembali ke menu utama): ")

                if paket_wisata_choice.lower() == 'back':
                    raise cExc.BackCommandInserted

                else:
                    data_paket_wisata = self._order_model.get_paket_wisata(paket_wisata_choice)
                    if data_paket_wisata:
                        new_order.set_paket_wisata(data_paket_wisata)

                        try:
                            tanggal_berangkat = input("Masukkan tanggal berangkat dengan format YYYY-MM-DD: ")
                            new_order.set_tanggal_berangkat(tanggal_berangkat)
                        except ValueError:
                            input("Format Tanggal Salah! Tekan Enter untuk mengulangi...")
                            continue

                        try:
                            jumlah_peserta = int(input("Ada berapa jumlah peserta? "))
                            if jumlah_peserta < 1:
                                raise ValueError
                        except ValueError:
                            input("Mohon untuk memasukkan bilangan yang valid! Tekan Enter untuk mengulangi...")
                            continue

                        daftar_peserta = list()
                        for peserta in range(jumlah_peserta):
                            nama_peserta = input("Nama Peserta: ")
                            ktp_peserta = input("No. KTP Peserta: ")
                            daftar_peserta.append({'nama_peserta': nama_peserta, 'no_ktp': ktp_peserta})
                        new_order.set_daftar_peserta(daftar_peserta)

                        confirm_order = input("Apa Anda yakin akan menambahkan order tersebut? [y/N]: ")
                        if confirm_order.lower() == 'y':
                            new_order.kode_booking = self.generate_kode_booking(new_order)
                            self._order_model.add_new_order_to_database(new_order, self.customer)
                            print(f"Kode Booking Anda: {new_order.kode_booking}")
                            input("Tekan Enter untuk kembali ke main menu...")
                            break
                        else:
                            input("Transaksi dibatalkan. Tekan Enter untuk kembali ke menu...")
                            break
                    else:
                        input("Paket Wisata tidak ditemukan. Tekan Enter untuk mengulangi...")
                        continue

            except cExc.BackCommandInserted:
                break

    def list_order_history(self):
        while True:
            try:
                order_history = self._cs_model.get_customer_order_history(self.customer.get_customer_id())
                View.order_history_list(order_history)
                choice = input("Masukkan pilihan (ketik 'back' untuk kembali ke menu utama) [1/2/back]: ")
                if choice.lower() == 'back':
                    raise cExc.BackCommandInserted
                elif choice == '1':
                    try:
                        kode_booking = input("Masukkan kode booking: ").upper()
                        order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
                        print()
                        View.order_detail(order_detail)
                        input("\nTekan Enter untuk melanjutkan...")
                    except cExc.OrderNotFound as e:
                        print(e)
                        input("\nTekan Enter untuk melanjutkan...")
                elif choice == '2':
                    break
                else:
                    input("Pilihan tidak tersedia. Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break

    def confirm_payment(self):
        while True:
            try:
                View.confirm_payment_dialog()
                kode_booking = input("Masukkan kode booking (ketik 'back' untuk kembali ke menu utama): ").upper()
                if kode_booking == 'BACK':
                    raise cExc.BackCommandInserted
                else:
                    order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
                    View.order_detail(order_detail)
                    kode_pembayaran = input("Masukkan nomor bukti pembayaran: ").upper()
                    confirm = input("Apakah Anda yakin akan melakukan pembayaran? [y/N]: ").upper()
                    if confirm == 'Y':
                        self._order_model.add_payment_proof(kode_booking, kode_pembayaran)
                        input("Transaksi berhasil. Tekan Enter untuk kembali ke menu...")
                        break
                    else:
                        input("Transaksi dibatalkan. Tekan Enter untuk kembali ke menu...")
                        break
            except cExc.OrderNotFound as e:
                print(e)
                input("Tekan Enter untuk kembali ke menu...")
                break
            except cExc.BackCommandInserted:
                break

    def cancel_order(self):
        while True:
            try:
                View.cancel_order_dialog()
                kode_booking = input("Masukkan kode booking (ketik 'back' untuk kembali ke menu utama): ").upper()
                if kode_booking == 'BACK':
                    raise cExc.BackCommandInserted
                else:
                    order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
                    View.order_detail(order_detail)

                    confirm = input("Apakah Anda ingin membatalkan order ini? [y/n]").upper()
                    if confirm == 'Y':
                        self._order_model.propose_order_cancel(kode_booking)
                        input("Berhasil mengajukan pembatalan. Tekan Enter untuk kembali ke menu...")
                        break
                    elif confirm == 'N':
                        input("Tekan Enter untuk kembali ke menu...")
                        break
            except cExc.OrderNotFound as e:
                print(e)
                input("Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break