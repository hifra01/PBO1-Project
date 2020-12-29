from abc import ABC, abstractmethod
from Models.OrderModel import OrderModel


class BaseController(ABC):
    def __init__(self, db_config_file):
        self._order_model: OrderModel = OrderModel(db_config_file)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def register(self):
        pass


if __name__ == '__main__':
    pass
