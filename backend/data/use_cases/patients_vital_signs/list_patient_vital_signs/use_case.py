from data.parameters.patients_vital_signs.list_patient_vital_signs import (
    ListPatientVitalSignsParameter,
)
from infra.repo.patients_vital_signs_repository.repository import (
    PatientsVitalSignsRepository,
)
from typing import Dict


class ListPatientVitalSignsUseCase:
    def __init__(self) -> None:
        self.__patients_vital_signs_repository = PatientsVitalSignsRepository()

    def execute(self, parameter: ListPatientVitalSignsParameter) -> Dict:
        patient_vital_signs_list = (
            self.__patients_vital_signs_repository.list_patient_vital_signs(
                patient_id=parameter.patient_id
            )
        )

        data_list = []
        for patient_vital_signs in patient_vital_signs_list:
            parsed_patient_vital_signs = patient_vital_signs._asdict()
            data_list.append(parsed_patient_vital_signs)

        return {"success": True, "data": data_list}
