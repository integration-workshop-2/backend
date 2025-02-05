from data.parameters.alarms.create_alarm.parameter import CreateAlarmParameter
from infra.repo.alarms_repository.repository import AlarmsRepository
from typing import Dict


class CreateAlarmUseCase:
    def __init__(self) -> None:
        self.__alarms_repository = AlarmsRepository()

    def execute(self, parameter: CreateAlarmParameter) -> Dict:
        created_alarm = self.__alarms_repository.create_alarm(
            patient_vital_signs_id=parameter.patient_vital_signs_id
        )

        return {"success": True, "data": created_alarm._asdict()}
