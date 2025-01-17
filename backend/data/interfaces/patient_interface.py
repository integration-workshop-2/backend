from abc import ABC, abstractmethod
from domain.models.patient_model import PatientModel
from typing import List


class PatientInterface(ABC):
    @abstractmethod
    def create_patient(cls, name: str) -> PatientModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def delete_patient(cls, id: str) -> PatientModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_patient(cls, id: str) -> PatientModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_patients(cls, name: str) -> List[PatientModel]:
        raise Exception("Method not implemented")

    @abstractmethod
    def update_patient(cls, id: str, name: str) -> PatientModel:
        raise Exception("Method not implemented")
