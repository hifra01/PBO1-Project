from db_connection import DBConnection


class Person:
    def __init__(self):
        self.email = ""
        self.person_id = ""
        self.name = ""
        self.role = ""
        self.db = DBConnection()

    def get_person_detail(self, email, password, role):
        query = "SELECT id, email, role FROM person WHERE email = %s AND password = %s AND role = %s"
        value = (email, password, role)
        result = self.db.select_one(query, value)
        return result

    def login(self, email, password):
        pass


class Customer(Person):
    def __init__(self):
        super().__init__()

    def login(self, email, password):
        person_detail = self.get_person_detail(email, password, 'customer')
        if person_detail is None:
            return False
        else:
            self.email = person_detail['email']
            self.person_id = person_detail['id']
            self.role = person_detail['role']


class Admin(Person):
    def __init__(self):
        super().__init__()
        self.admin_id = ""

    def login(self, email, password):
        person_detail = self.get_person_detail(email, password, 'admin')
        if person_detail is None:
            return False
        else:
            self.email = person_detail['email']
            self.person_id = person_detail['id']
            self.role = person_detail['role']

            query = "SELECT id, nama FROM admin WHERE person_id = %s"
            value = (self.person_id,)

            admin_detail = self.db.select_one(query, value)

            self.admin_id = admin_detail['id']
            self.name = admin_detail['nama']
