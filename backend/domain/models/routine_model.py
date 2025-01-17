from datetime import datetime
from typing import Literal, NamedTuple


class RoutineModel(NamedTuple):
    id: str
    patient_id: str
    medicine_id: str
    medicine_quantity: int
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    routine_description: str
    day_time: datetime
    created_at: datetime
    updated_at: datetime


class RoutineDataModel(NamedTuple):
    patient_name: str
    routine_description: str
