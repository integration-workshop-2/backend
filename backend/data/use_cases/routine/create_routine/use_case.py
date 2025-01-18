from data.parameters.routine.create_routine import CreateRoutineParameter
from infra.repo.routine_repository.repository import RoutineRepository
from typing import Dict


class CreateRoutineUseCase:
    def __init__(self) -> None:
        self.__routine_repository = RoutineRepository()

    def execute(self, parameter: CreateRoutineParameter) -> Dict:
        created_routine = self.__routine_repository.create_routine(
            patient_id=parameter.patient_id,
            medicine_id=parameter.medicine_id,
            medicine_quantity=parameter.medicine_quantity,
            week_day=parameter.week_day,
            day_time=parameter.day_time,
        )

        return {"success": True, "data": created_routine._asdict()}
