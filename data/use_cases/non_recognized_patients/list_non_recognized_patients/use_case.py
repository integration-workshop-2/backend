from infra.repo.non_recognized_patients_repository.repository import (
    NonRecognizedPatientsRepository,
)
from typing import Dict


class ListNonRecognizedPatientsUseCase:
    def __init__(self) -> None:
        self.__non_recognized_patients_repository = NonRecognizedPatientsRepository()

    def execute(self) -> Dict:
        non_recognized_patients_list = (
            self.__non_recognized_patients_repository.list_non_recognized_patient()
        )

        data_list = []
        for non_recognized_patient in non_recognized_patients_list:
            parsed_non_recognized_patient = non_recognized_patient._asdict()
            data_list.append(parsed_non_recognized_patient)

        return {"success": True, "data": data_list}
