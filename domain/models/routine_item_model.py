from datetime import datetime
from typing import Literal, NamedTuple


class RoutineItemDataModel(NamedTuple):
    patient_id: str
    patient_name: str
    routine_id: str
    routine_description: str


class RoutineItemModel(NamedTuple):
    id: str
    routine_id: str
    medicine_id: str
    medicine_quantity: str
    week_day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    day_time: str
    routine_description: str
    created_at: datetime
    updated_at: datetime
