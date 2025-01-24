from data.parameters.routine.create_routine.parameter import CreateRoutineParameter
from infra.repo.routine_items_repository.repository import RoutineItemsRepository
from infra.repo.routine_repository.repository import RoutineRepository
from infra.utils.crontab_util.util import CrontabUtil
from typing import Dict


class CreateRoutineUseCase:
    def __init__(self) -> None:
        self.__routine_repository = RoutineRepository()
        self.__routine_items_repository = RoutineItemsRepository()
        self.__crontab_service = CrontabUtil()

    def execute(self, parameter: CreateRoutineParameter) -> Dict:
        created_routine = self.__routine_repository.create_routine(
            patient_id=parameter.patient_id
        )

        created_routine_items_list = []
        for routine_item in parameter.routine_items_list:
            created_routine_item = self.__routine_items_repository.create_routine_item(
                routine_id=created_routine.id,
                medicine_id=routine_item.medicine_id,
                medicine_quantity=routine_item.medicine_quantity,
                week_day=routine_item.week_day,
                day_time=routine_item.day_time,
            )._asdict()

            self.__crontab_service.create_routine_job(
                routine_id=created_routine.id,
                medicine_id=routine_item.medicine_id,
                patient_id=parameter.patient_id,
                medicine_quantity=routine_item.medicine_quantity,
                week_day=routine_item.week_day,
                day_time=routine_item.day_time,
            )

            created_routine_items_list.append(created_routine_item)

        return {
            "success": True,
            "data": {
                "routine": created_routine._asdict(),
                "routine_items": created_routine_items_list,
            },
        }
