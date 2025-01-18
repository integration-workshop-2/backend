from data.parameters.routine_items.create_routine_item.parameter import (
    CreateRoutineItemParameter,
)
from data.parameters.routine.create_routine.parameter import CreateRoutineParameter
from infra.repo.routine_items_repository.repository import RoutineItemsRepository
from infra.repo.routine_repository.repository import RoutineRepository
from typing import Dict


class CreateRoutineUseCase:
    def __init__(self) -> None:
        self.__routine_repository = RoutineRepository()

    def execute(self, parameter: CreateRoutineParameter) -> Dict:
        created_routine = self.__routine_repository.create_routine(
            patient_id=parameter.patient_id
        )

        created_routine_items_list = []
        for routine_item in parameter.routine_items_list:
            parsed_routine_item = self.__routine_repository.create_routine_item(
                routine_id=created_routine.id,
                medicine_id=routine_item.medicine_id,
                medicine_quantity=routine_item.medicine_quantity,
                week_day=routine_item.week_day,
                day_time=routine_item.day_time,
            )
            created_routine_items_list.append(parsed_routine_item._asdict())

        return {
            "success": True,
            "data": {
                "routine": created_routine._asdict(),
                "routine_items": created_routine_items_list,
            },
        }
