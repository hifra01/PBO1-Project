from db_connection import DBConnection
import custom_exception as c_exc
from order import Order
from person import Customer


class CustomerModel(DBConnection):
    def __init__(self):
        super().__init__()

    def login(self, email: str, password: str) -> dict:
        query = "SELECT p.id as person_id, c.id as customer_id, p.role, " \
                "p.email, c.nama_lengkap, c.no_hp, c.no_ktp " \
                "FROM person p JOIN customers c on p.id = c.person_id " \
                "WHERE p.email = %s AND p.password = %s AND p.role = %s"
        value = (email, password, 'customer')
        result: dict = self.select_one(query, value)

        if result is None:
            raise c_exc.UserNotFound()
        else:
            return result

    def register_new_user(self, data: dict) -> None:
        # TODO: Tambah query untuk register customer baru, jangan lupa raise exception kalo ada error
        person_query = "INSERT INTO person (email, password, role) " \
                       "VALUES (%s, %s, 'customer')"
        person_value = (data['email'], data['password'])
        commit_person = self.execute(person_query, person_value)
        if commit_person:
            person_id = self.get_last_row_id()
            customer_query = "INSERT INTO customers " \
                             "(person_id, nama_lengkap, no_ktp, no_hp) " \
                             "VALUES (%s, %s, %s, %s)"
            customer_value = (person_id, data['nama'], data['no_ktp'], data['no_hp'])
            return self.execute(customer_query, customer_value)
        else:
            return commit_person

    def get_customer_order_history(self, customer_id: int) -> list:
        query = "SELECT o.kode_booking, oss.keterangan, pw.nama as paket_wisata, " \
                "o.tanggal_berangkat, o.tanggal_pulang " \
                "FROM `order` o JOIN paket_wisata pw on pw.id = o.id_paket_wisata " \
                "JOIN order_status_string oss on oss.id_status_order = o.id_status_order " \
                "WHERE o.customer = %s"
        value = (customer_id,)
        result = self.select_all(query, value)
        if result is None:
            return []
        else:
            return result


class AdminModel(DBConnection):
    def __init__(self):
        super().__init__()

    def login(self, email: str, password: str) -> dict:
        query = "SELECT p.id as person_id, a.id as admin_id, p.role, " \
                "p.email, a.nama " \
                "FROM person p JOIN admin a on p.id = a.person_id " \
                "WHERE p.email = %s AND p.password = %s AND p.role = %s"
        value = (email, password, 'admin')
        result: dict = self.select_one(query, value)

        if result is None:
            raise c_exc.UserNotFound()
        else:
            return result


class OrderModel(DBConnection):
    def __init__(self):
        super().__init__()

    def get_order_detail_by_booking_code(self, kode_booking: str) -> dict:
        detail: dict = dict()
        main_query: str = "SELECT o.id, o.kode_booking, oss.keterangan,o.id_paket_wisata, " \
                          "pw.nama as paket_wisata, o.tanggal_berangkat, o.tanggal_pulang " \
                          "FROM `order` o JOIN paket_wisata pw on pw.id = o.id_paket_wisata " \
                          "JOIN order_status_string oss on oss.id_status_order = o.id_status_order " \
                          "WHERE o.kode_booking = %s "
        main_value: tuple = (kode_booking,)
        main_result: dict = self.select_one(main_query, main_value)

        if main_result is None:
            raise c_exc.OrderNotFound()

        detail['kode_booking'] = main_result['kode_booking']
        detail['paket_wisata'] = main_result['paket_wisata']
        detail['status'] = main_result['keterangan']
        detail['tanggal_berangkat'] = main_result['tanggal_berangkat']
        detail['tanggal_pulang'] = main_result['tanggal_pulang']

        tempat_wisata_query: str = "SELECT dw.nama_tempat FROM destinasi_dalam_paket ddp " \
                                   "JOIN paket_wisata pw ON pw.id = ddp.paket " \
                                   "JOIN destinasi_wisata dw ON dw.id = ddp.destinasi " \
                                   "where pw.id = %s"
        tempat_wisata_value: tuple = (main_result['id_paket_wisata'],)

        tempat_wisata_result = self.select_all(tempat_wisata_query, tempat_wisata_value)
        detail['destinasi_wisata'] = list()
        detail['destinasi_wisata'] = tempat_wisata_result

        peserta_wisata_query = "SELECT nama_peserta, no_ktp FROM order_detail WHERE order_id = %s"
        peserta_wisata_value = (main_result['id'],)
        peserta_wisata_result = self.select_all(peserta_wisata_query, peserta_wisata_value)
        detail['peserta_wisata'] = peserta_wisata_result

        return detail

    def get_daftar_paket_wisata(self):
        paket_wisata_query = 'SELECT pw.id, pw.nama, pw.durasi FROM paket_wisata pw'
        paket_wisata_result = self.select_all(paket_wisata_query)
        return paket_wisata_result

    def get_paket_wisata(self, id_paket):
        paket_wisata_query = 'SELECT pw.id, pw.nama, pw.durasi FROM paket_wisata pw WHERE pw.id = %s'
        paket_wisata_value = (id_paket,)
        paket_wisata_result = self.select_one(paket_wisata_query, paket_wisata_value)
        return paket_wisata_result

    def add_new_order_to_database(self, order: Order, customer: Customer):
        order_query = "INSERT INTO `order` " \
                      "(kode_booking, customer, id_paket_wisata, id_status_order, " \
                      "tanggal_berangkat, tanggal_pulang) " \
                      "VALUES (%s, %s, %s, 'menunggu_pembayaran', " \
                      "%s, %s)"
        order_value = (order.kode_booking, customer.get_customer_id(),
                       order.id_paket_wisata, order.id_status_order,
                       order.tanggal_berangkat, order.tanggal_pulang)
        self.execute(order_query, order_value)

        new_order_id = self.get_last_row_id()
        daftar_peserta = list()
        for peserta in order.daftar_peserta:
            daftar_peserta.append((new_order_id, peserta['nama_peserta'], peserta['no_ktp']))

        daftar_peserta_query = "INSERT INTO order_detail (order_id, nama_peserta, no_ktp) " \
                               "VALUES (%s, %s, %s)"

        self.execute_many(daftar_peserta_query, daftar_peserta)

    def add_payment_proof(self, kode_booking, nomor_bukti):
        order_id_query = "SELECT id from `order` WHERE kode_booking = %s"
        order_id_value = (kode_booking,)
        order_id = self.select_one(order_id_query, order_id_value)

        if order_id:
            pembayaran_query = "INSERT INTO pembayaran (order_id, kode_bukti, status_verifikasi) " \
                               "VALUES (%s, %s, %s)"
            pembayaran_value = (order_id['id'], nomor_bukti, 'belum_verifikasi')
            self.execute(pembayaran_query, pembayaran_value)

            update_status_query = "UPDATE `order` " \
                                  "SET id_status_order='menunggu_verifikasi' " \
                                  "WHERE id = %s"
            update_status_value = (order_id['id'])
            self.execute(update_status_query, update_status_value)
        else:
            print("Order Not Found")

    def propose_order_cancel(self, kode_booking):
        order_id_query = "SELECT id from `order` WHERE kode_booking = %s"
        order_id_value = (kode_booking,)
        order_id = self.select_one(order_id_query, order_id_value)

        if order_id:
            cancel_query = "UPDATE `order` " \
                           "SET id_status_order='menunggu_pembatalan' " \
                           "WHERE id = %s"
            cancel_value = (order_id['id'])

            self.execute(cancel_query, cancel_value)
        else:
            print("Order Not Found")


if __name__ == "__main__":
    model = OrderModel()
    print(model.get_daftar_paket_wisata())
