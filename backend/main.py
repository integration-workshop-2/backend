from data.use_cases.routine.create_routine.use_case import CreateRoutineUseCase
from data.parameters.routine.create_routine.parameter import (
    CreateRoutineParameter,
    RoutineItem,
)

from data.use_cases.routine.delete_routine_items.use_case import (
    DeleteRoutineItemsUseCase,
)
from data.parameters.routine.delete_routine_items.parameter import (
    DeleteRoutineItemsParameter,
)


from datetime import time

if __name__ == "__main__":
    # use_case = CreateRoutineUseCase()
    # parameter = CreateRoutineParameter(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     routine_items_list=[
    #         RoutineItem(
    #             medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
    #             medicine_quantity=1,
    #             week_day="Monday",
    #             day_time=time(6, 0),
    #         ),
    #         RoutineItem(
    #             medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
    #             medicine_quantity=2,
    #             week_day="Tuesday",
    #             day_time=time(6, 0),
    #         ),
    #         RoutineItem(
    #             medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
    #             medicine_quantity=3,
    #             week_day="Wednesday",
    #             day_time=time(12, 0),
    #         ),
    #     ],
    # )

    # print(use_case.execute(parameter=parameter))

    use_case = DeleteRoutineItemsUseCase()
    parameter = DeleteRoutineItemsParameter(
        routine_items_ids_list=[
            "3d9f89f0-4e00-4268-a0e8-6bb30d2bd1b9",
            "6e38e243-4918-41ba-b40f-ca72c4f024f7",
        ]
    )
    print(use_case.execute(parameter=parameter))
