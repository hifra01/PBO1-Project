import mysql.connector
import yaml


class DBConnection:
    def __init__(self):
        """
        This class will load configuration from dbconfig.yaml file
        """
        try:
            with open("dbconfig.yaml", 'r') as stream:
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

    @property
    def cursor(self):
        return self.__cursor

    def select_one(self, query, value):
        self.cursor.execute(query, value)
        result = self.cursor.fetchone()
        return result


if __name__ == '__main__':
    db = DBConnection()
