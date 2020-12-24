from models import CustomerModel, AdminModel, OrderModel
from order import Order
from person import Customer, Admin
import custom_exception as c_exc
from view import View


class CustomerController:
    def __init__(self):
        self.customer: Customer = Customer()
        self._cs_model: CustomerModel = CustomerModel()
        self._order_model: OrderModel = OrderModel()

    def start(self):
        try:
            View.start()
            choice = input("Masukkan pilihanmu [1/2/exit]: ")
            if choice.lower() == 'exit':
                raise c_exc.ExitCommandInserted()
            elif choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            else:
                raise c_exc.UnknownCommand('Pilihan tidak valid.')
        except c_exc.UnknownCommand as e:
            print(e)
            input("Tekan Enter untuk melanjutkan")
            self.start()
        except Exception as e:
            print(f"Something's wrong, I can feel it. And here's what I got:\n{e}")

    def login(self) -> None:
        try:
            View.login_dialog()
            email: str = input("Masukkan email (ketik exit untuk keluar): ")
            if email.lower() == 'exit':
                raise c_exc.ExitCommandInserted()
            else:
                password: str = input("Masukkan password: ")
                self.customer.set_customer_data(self._cs_model.login(email=email, password=password))
                self.main_menu()
        except c_exc.ExitCommandInserted as e:
            print(e)

    def register(self):
        register_data = dict()
        register_data['nama'] = input("Masukkan Nama Lengkap: ")
        register_data['no_ktp'] = input("Masukkan Nomor KTP: ")
        register_data['no_hp'] = input("Masukkan Nomor HP: ")
        register_data['email'] = input("Masukkan E-mail: ")
        new_password = input("Masukkan Password baru: ")
        confirm_new_password = input('Konfirmasi Password baru Anda: ')

        if new_password == confirm_new_password:
            register_data['password'] = new_password
            self._cs_model.register_new_user(register_data)
        else:
            print("Password tidak sesuai!")

    def main_menu(self):
        View.main_menu_dialog()
        choice = input("Masukkan Pilihan [1/2/3/exit]: ")
        if choice.lower() == 'exit':
            raise c_exc.ExitCommandInserted()
        else:
            if choice == '1':
                self.new_order()
            elif choice == '2':
                self.list_order_history()
            elif choice == '3':
                pass
            else:
                print("Pilihan tidak valid")

    def new_order(self):
        new_order = Order()
        new_order.customer_id = self.customer.get_customer_id()

        daftar_paket_wisata = self._order_model.get_daftar_paket_wisata()
        View.list_paket_wisata(daftar_paket_wisata)
        paket_wisata_choice = input("Masukkan nomor paket wisata: ")

        data_paket_wisata = self._order_model.get_paket_wisata(paket_wisata_choice)
        new_order.set_paket_wisata(data_paket_wisata)

        tanggal_berangkat = input("Masukkan tanggal berangkat dengan format YYYY-MM-DD: ")
        new_order.set_tanggal_berangkat(tanggal_berangkat)

        jumlah_peserta = int(input("Ada berapa jumlah peserta? "))
        daftar_peserta = list()
        for peserta in range(jumlah_peserta):
            nama_peserta = input("Nama Peserta: ")
            ktp_peserta = input("No. KTP Peserta = ")
            daftar_peserta.append({'nama_peserta': nama_peserta, 'no_ktp': ktp_peserta})
        new_order.set_daftar_peserta(daftar_peserta)

        confirm_order = input("Apa Anda yakin akan menambahkan order tersebut? [y/n]")
        if confirm_order.lower() == 'y':
            self._order_model.add_new_order_to_database(new_order, self.customer)
            self.main_menu()
        elif confirm_order.lower() == 'n':
            input("Transaksi dibatalkan. Tekan Enter untuk kembali ke menu...")
            self.main_menu()

    def list_order_history(self):
        order_history = self._cs_model.get_customer_order_history(self.customer.get_customer_id())
        View.order_history_list(order_history)
        choice = input("Masukkan pilihan [1/2]: ")

        if choice == '1':
            kode_booking = input("Masukkan kode booking: ").upper()
            order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
            View.order_detail(order_detail)
            input("\n Tekan Enter untuk kembali")
            self.main_menu()
        elif choice == '2':
            self.main_menu()

    def confirm_payment(self):
        # TODO: Bikin customer method untuk konfirmasi pembayaran
        kode_booking = input("Masukkan kode booking: ").upper()
        order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
        View.order_detail(order_detail)
        kode_pembayaran = input("Masukkan nomor bukti pembayaran").upper()
        confirm = input("Apakah Anda yakin akan melakukan pembayaran? [y/n]").upper()
        if confirm == 'Y':
            self._order_model.add_payment_proof(kode_booking, kode_pembayaran)
            input("Transaksi berhasil. Tekan Enter untuk kembali ke menu...")
        elif confirm == 'N':
            input("Transaksi dibatalkan. Tekan Enter untuk kembali ke menu...")
            self.main_menu()

    def cancel_order(self):
        # TODO: Bikin customer method untuk membatalkan pesanan
        kode_booking = input("Masukkan kode booking: ").upper()
        order_detail = self._order_model.get_order_detail_by_booking_code(kode_booking)
        View.order_detail(order_detail)

        confirm = input("Apakah Anda ingin membatalkan order ini? [y/n]").upper()
        if confirm == 'Y':

            pass
        elif confirm == 'N':
            input("Tekan Enter untuk kembali ke menu...")
            self.main_menu()
        pass


class AdminController:
    def __init__(self):
        self.admin: Admin = Admin()
        self.__admin_model: AdminModel = AdminModel()

    def start(self):
        try:
            View.login_dialog()
            email: str = input("Masukkan email (ketik exit untuk keluar): ")
            if email.lower() == 'exit':
                raise c_exc.ExitCommandInserted()
            else:
                password: str = input("Masukkan password: ")
                self.admin.set_admin_data(self.__admin_model.login(email=email, password=password))
                self.main_menu()
        except c_exc.ExitCommandInserted as e:
            print(e)
        except Exception as e:
            print(e)
            self.start()

    def main_menu(self):
        # TODO: Bikin main menu admin
        pass


if __name__ == '__main__':
    console = CustomerController()
    console.start()
