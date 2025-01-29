import argparse

from data.parameters.routine_trigger.execute_routine_trigger.parameter import (
    RoutineTriggerArgsParameter,
)
from data.use_cases.routine_trigger.execute_routine_trigger.use_case import (
    ExecuteRoutineTriggerUseCase,
)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--medicine_id", type=str, required=True)
    argparser.add_argument("--medicine_quantity", type=int, required=True)
    argparser.add_argument("--patient_id", type=str, required=True)
    args = argparser.parse_args()

    use_case = ExecuteRoutineTriggerUseCase()
    parameter = RoutineTriggerArgsParameter(**args.__dict__)
    use_case.execute(parameter=parameter)
