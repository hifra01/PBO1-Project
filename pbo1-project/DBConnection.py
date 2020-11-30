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
        except FileNotFoundError as e:
            print(e)
        except yaml.YAMLError as e:
            print(e)
        except mysql.connector.Error as e:
            print(e.msg)

    @property
    def con(self):
        return self.__con


if __name__ == '__main__':
    db = DBConnection()
