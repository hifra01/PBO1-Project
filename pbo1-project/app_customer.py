from Controllers import CustomerController
import os.path as path

if __name__ == '__main__':
    db_config_file = path.join(path.dirname(path.abspath(__file__)), 'dbconfig.yaml')
    app = CustomerController(db_config_file)
    app.start()
