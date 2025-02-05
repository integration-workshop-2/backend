from data.parameters.non_recognized_patients.create_non_recognized_patient.parameter import (
    CreateNonRecognizedPatientParameter,
)
from infra.repo.non_recognized_patients_repository.repository import (
    NonRecognizedPatientsRepository,
)
from typing import Dict


class CreateNonRecognizedPatientUseCase:
    def __init__(self) -> None:
        self.__non_recognized_patients_repository = NonRecognizedPatientsRepository()

    def execute(self, parameter: CreateNonRecognizedPatientParameter) -> Dict:
        non_recognized_patient = (
            self.__non_recognized_patients_repository.create_non_recognized_patient(
                patient_id=parameter.patient_id
            )
        )

        return {"success": True, "data": non_recognized_patient._asdict()}
