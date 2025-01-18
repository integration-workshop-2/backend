from data.use_cases.alarms.create_alarm.use_case import CreateAlarmUseCase
from data.parameters.alarms.create_alarm.parameter import CreateAlarmParameter

from data.use_cases.alarms.list_alarms.use_case import ListAlarmsUseCase


if __name__ == "__main__":
    use_case = ListAlarmsUseCase()
    print(use_case.execute())
