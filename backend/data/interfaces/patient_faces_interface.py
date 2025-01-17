from abc import ABC, abstractmethod
from domain.models.patient_faces_model import PatientFacesModel
from typing import List


class PatientFacesInterface(ABC):
    @abstractmethod
    def create_patient_faces(
        cls, patient_id: str, face_embedding: List[float]
    ) -> PatientFacesModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_patient_faces_by_patient_id(
        cls, patient_id: str
    ) -> List[PatientFacesModel]:
        raise Exception("Method not implemented")
