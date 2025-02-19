from data.parameters.patient.delete_patient.parameter import DeletePatientParameter
from infra.repo.patient_repository.repository import PatientRepository
from infra.utils.crontab_util.util import CrontabUtil
from typing import Dict


class DeletePatientUseCase:
    def __init__(self) -> None:
        self.__crontab_util = CrontabUtil()
        self.__patient_repository = PatientRepository()

    def execute(self, parameter: DeletePatientParameter) -> Dict:
        deleted_patient = self.__patient_repository.delete_patient(
            id=parameter.patient_id
        )

        self.__crontab_util.delete_routine_job_by_patient_id(
            patient_id=parameter.patient_id
        )

        return {"success": True, "data": deleted_patient._asdict()}
