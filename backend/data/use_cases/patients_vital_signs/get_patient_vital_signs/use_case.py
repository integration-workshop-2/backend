from data.parameters.patients_vital_signs.get_patient_vital_signs import (
    GetPatientVitalSignsParameter,
)
from infra.repo.patients_vital_signs_repository.repository import (
    PatientsVitalSignsRepository,
)
from typing import Dict


class GetPatientVitalSignsUseCase:
    def __init__(self) -> None:
        self.__patients_vital_signs_repository = PatientsVitalSignsRepository()

    def execute(self, parameter: GetPatientVitalSignsParameter) -> Dict:
        patient_vital_signs = (
            self.__patients_vital_signs_repository.get_patient_vital_signs(
                id=parameter.id
            )
        )

        return {"success": True, "data": patient_vital_signs._asdict()}
