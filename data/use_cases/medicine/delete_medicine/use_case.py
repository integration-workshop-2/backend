from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter
from infra.repo.medicine_repository.repository import MedicineRepository
from infra.utils.crontab_util.util import CrontabUtil
from typing import Dict


class DeleteMedicineUseCase:
    def __init__(self) -> None:
        self.__crontab_util = CrontabUtil()
        self.__medicine_repository = MedicineRepository()

    def execute(self, parameter: DeleteMedicineParameter) -> Dict:
        deleted_medicine = self.__medicine_repository.delete_medicine(
            id=parameter.medicine_id
        )

        self.__crontab_util.delete_routine_job_by_medicine_id(
            medicine_id=parameter.medicine_id
        )

        return {"success": True, "data": deleted_medicine._asdict()}
