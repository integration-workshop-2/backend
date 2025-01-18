from datetime import time
from typing import Literal, NamedTuple


class CreateRoutineParameter(NamedTuple):
    patient_id: str
    medicine_id: str
    medicine_quantity: int
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    day_time: time
