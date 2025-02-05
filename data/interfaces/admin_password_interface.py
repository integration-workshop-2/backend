from abc import ABC, abstractmethod
from domain.models.admin_password_model import AdminPasswordModel


class AdminPasswordInterface(ABC):
    @abstractmethod
    def get_admin_password(cls) -> AdminPasswordModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def update_admin_password(cls, password: str) -> AdminPasswordModel:
        raise Exception("Method not implemented")
