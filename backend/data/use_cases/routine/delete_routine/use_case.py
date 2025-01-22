from data.parameters.routine.delete_routine.parameter import DeleteRoutineParameter
from infra.repo.routine_repository.repository import RoutineRepository
from infra.utils.crontab_util.util import CrontabUtil
from typing import Dict


class DeleteRoutineUseCase:
    def __init__(self) -> None:
        self.__crontab_util = CrontabUtil()
        self.__routine_repository = RoutineRepository()

    def execute(self, parameter: DeleteRoutineParameter) -> Dict:
        deleted_routine = self.__routine_repository.delete_routine(
            id=parameter.routine_id
        )

        self.__crontab_util.delete_routine_job(routine_id=parameter.routine_id)

        return {"success": True, "data": deleted_routine._asdict()}
