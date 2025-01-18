from data.parameters.patient.update_patient import UpdatePatientParameter
from infra.repo.patient_repository.repository import PatientRepository
from typing import Dict


class UpdatePatientUseCase:
    def __init__(self) -> None:
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: UpdatePatientParameter) -> Dict:
        updated_patient = self.__patient_repository.update_patient(
            id=parameter.patient_id, name=parameter.name
        )

        return {"success": True, "data": updated_patient._asdict()}
