from data.use_cases.routine.create_routine.use_case import CreateRoutineUseCase
from data.parameters.routine.create_routine.parameter import (
    CreateRoutineParameter,
    RoutineItemParameter,
)

from data.use_cases.routine.delete_routine_items.use_case import (
    DeleteRoutineItemsUseCase,
)
from data.parameters.routine.delete_routine_items.parameter import (
    DeleteRoutineItemsParameter,
)

from data.use_cases.patient.create_patient.use_case import CreatePatientUseCase
from data.parameters.patient.create_patient.parameter import CreatePatientParameter
from data.use_cases.medicine.create_medicine import CreateMedicineUseCase
from data.parameters.medicine.create_medicine import CreateMedicineParameter

from datetime import time

if __name__ == "__main__":
    use_case = CreateRoutineUseCase()
    parameter = CreateRoutineParameter(
        patient_id="0becd8d4-9caa-4194-82eb-3c407740400e",
        routine_items_list=[
            RoutineItemParameter(
                medicine_id="27d44d08-6fa2-4c89-8741-e7f8eb489b40",
                medicine_quantity=1,
                week_day="Monday",
                day_time=time(6, 0),
            ),
            RoutineItemParameter(
                medicine_id="27d44d08-6fa2-4c89-8741-e7f8eb489b40",
                medicine_quantity=2,
                week_day="Tuesday",
                day_time=time(6, 0),
            ),
            RoutineItemParameter(
                medicine_id="27d44d08-6fa2-4c89-8741-e7f8eb489b40",
                medicine_quantity=3,
                week_day="Wednesday",
                day_time=time(12, 0),
            ),
        ],
    )

    print(use_case.execute(parameter=parameter))
