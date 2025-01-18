from data.parameters.patient.list_patients import ListPatientsParameter
from infra.repo.patient_repository.repository import PatientRepository
from typing import Dict


class ListPatientsUseCase:
    def __init__(self) -> None:
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: ListPatientsParameter) -> Dict:
        patients_list = self.__patient_repository.list_patients(
            name=parameter.patient_name
        )

        data_list = []
        for patient in patients_list:
            parsed_patient = patient._asdict()
            data_list.append(parsed_patient)

        return {"success": True, "data": data_list}
