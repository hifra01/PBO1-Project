import os.path as path
import mysql.connector
import yaml


class DBConnection:
    def __init__(self):
        """
        This class will load MySQL database configuration from dbconfig.yaml file
        """
        try:
            config_file = path.join(path.dirname(path.abspath(__file__)), 'dbconfig.yaml')
            with open(config_file, 'r') as stream:
                dbconfig = yaml.safe_load(stream)['dbconfig']
                self.__con = mysql.connector.connect(
                    user=dbconfig['user'],
                    password=dbconfig['password'],
                    host=dbconfig['host'],
                    database=dbconfig['database']
                )
                self.__cursor = self.__con.cursor(dictionary=True)
        except FileNotFoundError as e:
            print(e)
        except yaml.YAMLError as e:
            print(e)
        except mysql.connector.Error as e:
            print(e.msg)

    def select_one(self, query, value=tuple()):
        self.__cursor.execute(query, value)
        result = self.__cursor.fetchone()
        self.__con.commit()
        return result

    def select_all(self, query, value=tuple()):
        self.__cursor.execute(query, value)
        result = self.__cursor.fetchall()
        self.__con.commit()
        return result

    def execute(self, query, value=tuple()):
        try:
            self.__cursor.execute(query, value)
            self.__con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def execute_many(self, query, value=tuple()):
        try:
            self.__cursor.executemany(query, value)
            self.__con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_last_row_id(self):
        result = self.__cursor.lastrowid
        self.__con.commit()
        return result


if __name__ == '__main__':
    pass
