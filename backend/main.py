from data.use_cases.alarms.create_alarm.use_case import CreateAlarmUseCase
from data.parameters.alarms.create_alarm.parameter import CreateAlarmParameter

if __name__ == "__main__":
    use_case = CreateAlarmUseCase()
    parameter = CreateAlarmParameter(
        patient_vital_signs_id="b11450ac-5f5b-4536-a6c9-23f32ec0a5e3"
    )
    print(use_case.execute(parameter=parameter))
