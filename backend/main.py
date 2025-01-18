from data.use_cases.routine.create_routine.use_case import CreateRoutineUseCase
from data.parameters.routine.create_routine.parameter import CreateRoutineParameter

from datetime import time

if __name__ == "__main__":
    use_case = CreateRoutineUseCase()
    parameter = CreateRoutineParameter(
        patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
        medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
        medicine_quantity=3,
        week_day="Monday",
        day_time=time(23, 44),
    )

    print(use_case.execute(parameter=parameter))
