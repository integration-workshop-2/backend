from data.parameters.patient.get_patient import GetPatientParameter
from infra.repo.patient_repository.repository import PatientRepository
from typing import Dict


class GetPatientUseCase:
    def __init__(self) -> None:
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: GetPatientParameter) -> Dict:
        patient = self.__patient_repository.get_patient(id=parameter.patient_id)

        return {"success": True, "data": patient._asdict()}
