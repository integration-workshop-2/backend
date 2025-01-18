from data.parameters.patient.delete_patient import DeletePatientParameter
from infra.repo.patient_repository.repository import PatientRepository
from typing import Dict


class DeletePatientUseCase:
    def __init__(self) -> None:
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: DeletePatientParameter) -> Dict:
        deleted_patient = self.__patient_repository.delete_patient(
            id=parameter.patient_id
        )

        return {"success": True, "data": deleted_patient._asdict()}
