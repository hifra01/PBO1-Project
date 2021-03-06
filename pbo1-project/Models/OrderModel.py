from .DBConnection import DBConnection
import CustomExceptions as cExc
from Orders import Order
from Persons import Customer, Admin


class OrderModel(DBConnection):
    def __init__(self, db_config_file):
        super().__init__(db_config_file)

    def get_order_id_from_booking_code(self, kode_booking):
        order_id_query = "SELECT id from `order` WHERE kode_booking = %s"
        order_id_value = (kode_booking,)
        order_id = self.select_one(order_id_query, order_id_value)
        if order_id:
            return order_id['id']
        else:
            return None

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
            raise cExc.OrderNotFound()

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
                      "VALUES (%s, %s, %s, %s, " \
                      "%s, %s)"
        order_value = (order.kode_booking, customer.get_customer_id(),
                       order.id_paket_wisata, 'menunggu_pembayaran',
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
            update_status_value = (order_id['id'],)
            self.execute(update_status_query, update_status_value)
        else:
            raise cExc.OrderNotFound

    def propose_order_cancel(self, kode_booking):
        order_id_query = "SELECT id from `order` WHERE kode_booking = %s"
        order_id_value = (kode_booking,)
        order_id = self.select_one(order_id_query, order_id_value)

        if order_id:
            cancel_query = "UPDATE `order` " \
                           "SET id_status_order='menunggu_pembatalan' " \
                           "WHERE id = %s"
            cancel_value = (order_id['id'],)

            self.execute(cancel_query, cancel_value)
        else:
            raise cExc.OrderNotFound

    def get_city_id_from_paket_wisata(self, order: Order):
        query = "SELECT kota FROM paket_wisata WHERE id = %s"
        value = (order.id_paket_wisata,)
        result = self.select_one(query, value)
        return result['kota']

    def get_last_order_id(self):
        query = "SELECT MAX(id) as last_id FROM `order`"
        result = self.select_one(query)
        return result['last_id']

    def get_orders_waiting_payment_information(self):
        query = "SELECT o.kode_booking, c.nama_lengkap as customer, " \
                "o.created_date, oss.keterangan " \
                "FROM `order` o " \
                "JOIN order_status_string oss on o.id_status_order = oss.id_status_order " \
                "JOIN customers c on c.id = o.customer " \
                "WHERE o.id_status_order='menunggu_verifikasi'"
        result = self.select_all(query)
        return result

    def get_orders_waiting_cancel_confirmation(self):
        query = "SELECT o.kode_booking, c.nama_lengkap AS customer, " \
                "o.created_date, oss.keterangan " \
                "FROM `order` o " \
                "JOIN order_status_string oss on o.id_status_order = oss.id_status_order " \
                "JOIN customers c on c.id = o.customer " \
                "WHERE o.id_status_order='menunggu_pembatalan'"
        result = self.select_all(query)
        return result

    def get_order_with_payment_from_booking_code(self, kode_booking):
        order_id = self.get_order_id_from_booking_code(kode_booking)
        if order_id:
            query = "SELECT o.id, o.kode_booking, p.kode_bukti, c.nama_lengkap as customer, " \
                    "o.created_date, oss.keterangan " \
                    "FROM `order` o " \
                    "JOIN order_status_string oss ON o.id_status_order = oss.id_status_order " \
                    "JOIN customers c ON c.id = o.customer " \
                    "JOIN pembayaran p ON o.id = p.order_id " \
                    "WHERE o.id_status_order='menunggu_verifikasi' " \
                    "AND o.id = %s " \
                    "ORDER BY p.id desc "
            value = (order_id,)
            result = self.select_one(query, value)
            if result:
                return result
            else:
                raise cExc.OrderNotFound
        else:
            raise cExc.OrderNotFound

    def verify_order_payment(self, kode_booking, admin: Admin):
        order_id = self.get_order_id_from_booking_code(kode_booking)
        if order_id:
            query = "UPDATE pembayaran SET status_verifikasi=%s, petugas_verifikasi=%s " \
                    "WHERE order_id=%s"
            value = ('telah_verifikasi', admin.get_admin_id(), order_id)
            self.execute(query, value)

            order_query = "UPDATE `order` SET id_status_order = 'terbayar' " \
                          "WHERE id=%s"
            order_value = (order_id,)
            self.execute(order_query, order_value)

    def confirm_order_cancel(self, kode_booking):
        order_id = self.get_order_id_from_booking_code(kode_booking)
        if order_id:
            query = "UPDATE `order` SET id_status_order='dibatalkan' " \
                    "WHERE id = %s"
            value = (order_id,)
            self.execute(query, value)
