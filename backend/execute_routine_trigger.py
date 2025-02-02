import argparse

from data.parameters.routine_trigger.execute_routine_trigger.parameter import (
    RoutineTriggerArgsParameter,
)
from data.use_cases.routine_trigger.execute_routine_trigger.use_case import (
    ExecuteRoutineTriggerUseCase,
)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--execution_pattern", type=str, required=True)
    args = argparser.parse_args()

    use_case = ExecuteRoutineTriggerUseCase()
    parameter = RoutineTriggerArgsParameter(**args.__dict__)
    use_case.execute(parameter=parameter)
