from abc import ABC, abstractmethod


class AdminPasswordInterface(ABC):
    @abstractmethod
    def update_admin_password(cls, password: str) -> None:
        raise Exception("Method not implemented")
