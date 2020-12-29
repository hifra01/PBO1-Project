from getpass import getpass
from .BaseController import BaseController
from Persons import Admin
from Models import AdminModel
from Views import View
import CustomExceptions as cExc


class AdminController(BaseController):
    def __init__(self, db_config_file):
        super().__init__(db_config_file)
        self.admin: Admin = Admin()
        self.__admin_model: AdminModel = AdminModel(db_config_file)

    def start(self):
        try:
            self.login()
        except KeyboardInterrupt:
            print("Force quit app.")

    def login(self):
        while True:
            try:
                View.login_dialog()
                email: str = input("Masukkan email (ketik exit untuk keluar): ")
                if email.lower() == 'exit':
                    raise cExc.ExitCommandInserted()
                else:
                    password: str = getpass("Masukkan password: ")
                    self.admin.set_admin_data(self.__admin_model.login(email=email, password=password))
                    self.main_menu()
            except cExc.ExitCommandInserted as e:
                print(e)
                break
            except cExc.UserNotFound as e:
                print(e)
                input("Tekan Enter untuk melanjutkan...")

    def register(self):
        while True:
            try:
                View.add_new_admin_dialog()
                register_data = dict()
                nama_input = input("Masukkan Nama (ketik 'back' untuk kembali ke menu utama): ")
                if nama_input.lower() == 'back':
                    raise cExc.BackCommandInserted
                else:
                    register_data['nama'] = nama_input
                    register_data['email'] = input("Masukkan E-mail: ")
                    new_password = getpass("Masukkan Password baru: ")
                    confirm_new_password = getpass('Konfirmasi Password baru Anda: ')
                    if new_password == confirm_new_password:
                        confirm = input("Apakah Anda ingin mendaftarkan akun tersebut? [y/N]")
                        if confirm.lower() == 'y':
                            register_data['password'] = new_password
                            self.__admin_model.register_new_user(register_data)
                            input("Pendaftaran berhasil. Tekan Enter untuk kembali ke menu...")
                        else:
                            input("Pendaftaran dibatalkan. Tekan Enter untuk kembali ke menu...")
                        break
                    else:
                        input("Password tidak sesuai. Tekan Enter untuk mengulangi...")
            except cExc.BackCommandInserted:
                break

    def main_menu(self):
        while True:
            View.admin_main_menu_dialog()
            choice = input("Masukkan Pilihan [1/2/3/4/5/exit]: ")
            if choice.lower() == 'exit':
                raise cExc.ExitCommandInserted()
            else:
                if choice == '1':
                    self.lihat_order_menunggu_verifikasi_pembayaran()
                elif choice == '2':
                    self.verifikasi_pembayaran_order()
                elif choice == '3':
                    self.lihat_order_menunggu_pembatalan()
                elif choice == '4':
                    self.konfirmasi_pembatalan_order()
                elif choice == '5':
                    self.register()
                else:
                    input("Pilihan tidak valid. Tekan Enter untuk melanjutkan...")
        pass

    def lihat_order_menunggu_verifikasi_pembayaran(self):
        orders = self._order_model.get_orders_waiting_payment_information()
        View.orders_waiting_confirmation(orders)
        input("Tekan Enter untuk kembali ke menu...")

    def verifikasi_pembayaran_order(self):
        while True:
            try:
                View.verify_payment_code_dialog()
                kode_booking = input("Masukkan kode booking (ketik 'back' untuk kembali ke menu utama): ").upper()
                if kode_booking == 'BACK':
                    raise cExc.BackCommandInserted
                else:
                    order_detail = self._order_model.get_order_with_payment_from_booking_code(kode_booking)
                    View.verify_payment_order_detail(order_detail)
                    verify = input("Verifikasi pembayaran ini? [y/N] ").upper()

                    if verify == 'Y':
                        self._order_model.verify_order_payment(kode_booking, self.admin)
                        input("Verifikasi berhasil. Tekan Enter untuk kembali ke menu utama...")
                    else:
                        input("Verifikasi dibatalkan. Tekan Enter untuk kembali ke menu utama...")
                break
            except cExc.OrderNotFound as e:
                print(e)
                input("Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break

    def lihat_order_menunggu_pembatalan(self):
        orders = self._order_model.get_orders_waiting_cancel_confirmation()
        View.orders_waiting_confirmation(orders)
        input("Tekan Enter untuk kembali ke menu...")

    def konfirmasi_pembatalan_order(self):
        while True:
            try:
                View.confirm_order_cancel_dialog()
                kode_booking = input("Masukkan kode booking (ketik 'back' untuk kembali ke menu utama): ").upper()
                if kode_booking == 'BACK':
                    raise cExc.BackCommandInserted
                else:
                    order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
                    View.order_detail(order_detail)
                    verify = input("Batalkan pembayaran ini? [y/N] ").upper()

                    if verify == 'Y':
                        self._order_model.confirm_order_cancel(kode_booking)
                        input("Pembatalan berhasil. Tekan Enter untuk kembali ke menu utama...")
                    else:
                        input("Pembatalan dibatalkan. Tekan Enter untuk kembali ke menu utama...")
                break
            except cExc.OrderNotFound as e:
                print(e)
                input("Tekan Enter untuk melanjutkan...")
            except cExc.BackCommandInserted:
                break