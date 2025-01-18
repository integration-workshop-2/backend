from abc import ABC, abstractmethod
from domain.models.patients_vital_signs_model import PatientsVitalSignsModel
from typing import List


class PatientsVitalSignalsInterface(ABC):
    @abstractmethod
    def create_patient_vital_signs(
        cls, patient_id: str, bpm: int, oxygenation_percentage: int
    ) -> PatientsVitalSignsModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_patient_vital_signs(cls, id: str) -> PatientsVitalSignsModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_patient_vital_signs(cls, patient_id: str) -> List[PatientsVitalSignsModel]:
        raise Exception("Method not implemented")
