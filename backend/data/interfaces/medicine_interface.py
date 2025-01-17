from abc import ABC, abstractmethod
from domain.models.medicine_model import MedicineModel
from typing import List


class MedicineInterface(ABC):
    @abstractmethod
    def create_medicine(cls, name: str, cylinder_number: int) -> MedicineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def delete_medicine(cls, id: str) -> MedicineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_medicine(cls, id: str) -> MedicineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_medicine(cls) -> List[MedicineModel]:
        raise Exception("Method not implemented")

    @abstractmethod
    def update_medicine(cls, id: str, name: str, cylinder_number: int) -> MedicineModel:
        raise Exception("Method not implemented")
