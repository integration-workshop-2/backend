from data.parameters.routine.create_routine import CreateRoutineParameter, RoutineItem
from infra.repo.routine_repository.repository import RoutineRepository
from typing import Dict


class CreateRoutineUseCase:
    def __init__(self) -> None:
        self.__routine_repository = RoutineRepository()

    def execute(self, parameter: CreateRoutineParameter) -> Dict:
        routine_items_list = parameter.routine_items_list

        created_routine_items_list = []
        for routine_item in routine_items_list:
            parsed_routine_item = self.__routine_repository.create_routine(
                patient_id=parameter.patient_id,
                medicine_id=routine_item.medicine_id,
                medicine_quantity=routine_item.medicine_quantity,
                week_day=routine_item.week_day,
                day_time=routine_item.day_time,
            )
            created_routine_items_list.append(parsed_routine_item._asdict())

        return {"success": True, "data": created_routine_items_list}
