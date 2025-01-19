from datetime import time
from typing import List, Literal, NamedTuple


class CrateRoutineItemParameter(NamedTuple):
    medicine_id: str
    medicine_quantity: int
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    day_time: time


class CreateRoutineParameter(NamedTuple):
    patient_id: str
    routine_items_list: List[CrateRoutineItemParameter]
