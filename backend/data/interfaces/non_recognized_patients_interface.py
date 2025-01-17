from abc import ABC, abstractmethod
from domain.models.non_recognized_patients_model import NonRecognizedPatientsModel
from typing import List


class NonRecognizedPatientsInterface(ABC):
    @abstractmethod
    def create_non_recognized_patient(
        cls, patient_id: str
    ) -> NonRecognizedPatientsModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_non_recognized_patient(cls, id: str) -> NonRecognizedPatientsModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_non_recognized_patient(cls) -> List[NonRecognizedPatientsModel]:
        raise Exception("Method not implemented")
