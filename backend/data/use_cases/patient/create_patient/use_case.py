from data.parameters.patient.create_patient.parameter import CreatePatientParameter
from infra.repo.patient_faces_repository.repository import PatientFacesRepository
from infra.repo.patient_repository.repository import PatientRepository
from typing import Dict


class CreatePatientUseCase:
    def __init__(self) -> None:
        self.__patient_faces_repository = PatientFacesRepository()
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: CreatePatientParameter) -> Dict:
        created_patient = self.__patient_repository.create_patient(name=parameter.name)

        for face_embedding in parameter.face_embeddings:
            self.__patient_faces_repository.create_patient_faces(
                patient_id=created_patient.id, face_embedding=face_embedding
            )

        return {"success": True, "data": created_patient._asdict()}
