from Controllers import AdminController
import os.path as path

if __name__ == '__main__':
    db_config_file = path.join(path.dirname(path.abspath(__file__)), 'dbconfig.yaml')
    app = AdminController(db_config_file)
    app.start()
