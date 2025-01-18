from datetime import datetime, time
from typing import Literal, NamedTuple


class RoutineItemDataModel(NamedTuple):
    patient_name: str
    routine_description: str


class RoutineItemModel(NamedTuple):
    id: str
    routine_id: str
    medicine_id: str
    medicine_quantity: str
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    day_time: time
    routine_description: str
    created_at: datetime
    updated_at: datetime
