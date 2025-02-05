from datetime import time
from typing import List, Literal, NamedTuple


class UpdateRoutineItemParameter(NamedTuple):
    medicine_id: str
    medicine_quantity: int
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    day_time: time


class UpdateRoutineParameter(NamedTuple):
    patient_id: str
    routine_id: str
    routine_items_list: List[UpdateRoutineItemParameter]
