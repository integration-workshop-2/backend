from data.parameters.patients_vital_signs.create_patient_vital_signs import (
    CreatePatientVitalSignsParameter,
)
from infra.repo.patients_vital_signs_repository.repository import (
    PatientsVitalSignsRepository,
)
from typing import Dict


class CreatePatientVitalSignsUseCase:
    def __init__(self) -> None:
        self.__patients_vital_signs_repository = PatientsVitalSignsRepository()

    def execute(self, parameter: CreatePatientVitalSignsParameter) -> Dict:
        created_patient_vital_signs = (
            self.__patients_vital_signs_repository.create_patient_vital_signs(
                patient_id=parameter.patient_id,
                bpm=parameter.bpm,
                oxygenation_percentage=parameter.oxygenation_percentage,
            )
        )

        return {"success": True, "data": created_patient_vital_signs._asdict()}
