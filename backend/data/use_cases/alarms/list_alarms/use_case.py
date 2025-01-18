from infra.repo.alarms_repository.repository import AlarmsRepository
from typing import Dict


class ListAlarmsUseCase:
    def __init__(self) -> None:
        self.__alarms_repository = AlarmsRepository()

    def execute(self) -> Dict:
        alarms_list = self.__alarms_repository.list_alarms()

        data_list = []
        for alarm in alarms_list:
            parsed_alarm = alarm._asdict()
            data_list.append(parsed_alarm)

        return {"success": True, "data": data_list}
