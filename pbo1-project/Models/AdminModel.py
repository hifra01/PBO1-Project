from .DBConnection import DBConnection
from .PersonModel import PersonModel
import CustomExceptions as cExc


class AdminModel(DBConnection, PersonModel):
    def __init__(self, db_config_file):
        super().__init__(db_config_file)

    def login(self, email: str, password: str) -> dict:
        query = "SELECT p.id as person_id, a.id as admin_id, p.role, " \
                "p.email, a.nama " \
                "FROM person p JOIN admin a on p.id = a.person_id " \
                "WHERE p.email = %s AND p.password = %s AND BINARY(p.password) = %s AND p.role = %s"
        value = (email, password, password, 'admin')
        result: dict = self.select_one(query, value)

        if result is None:
            raise cExc.UserNotFound()
        else:
            return result

    def register_new_user(self, data: dict) -> None:
        person_query = "INSERT INTO person (email, password, role) " \
                       "VALUES (%s, %s, 'admin')"
        person_value = (data['email'], data['password'])
        commit_person = self.execute(person_query, person_value)
        if commit_person:
            person_id = self.get_last_row_id()
            admin_query = "INSERT INTO `admin` " \
                          "(person_id, nama) " \
                          "VALUES (%s, %s)"
            admin_value = (person_id, data['nama'])
            return self.execute(admin_query, admin_value)
        else:
            return commit_person
