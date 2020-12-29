from .DBConnection import DBConnection
from .PersonModel import PersonModel
import CustomExceptions as cExc


class CustomerModel(DBConnection, PersonModel):
    def __init__(self, db_config_file):
        super().__init__(db_config_file)

    def login(self, email: str, password: str) -> dict:
        query = "SELECT p.id as person_id, c.id as customer_id, p.role, " \
                "p.email, c.nama_lengkap, c.no_hp, c.no_ktp " \
                "FROM person p JOIN customers c on p.id = c.person_id " \
                "WHERE p.email = %s AND p.password = %s AND BINARY(p.password) = %s AND p.role = %s"
        value = (email, password, password, 'customer')
        result: dict = self.select_one(query, value)

        if result is None:
            raise cExc.UserNotFound()
        else:
            return result

    def register_new_user(self, data: dict) -> None:
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
