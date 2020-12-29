from abc import ABC, abstractmethod


class PersonModel(ABC):
    @abstractmethod
    def login(self, email: str, password: str):
        pass

    def register_new_user(self, data: dict):
        pass
