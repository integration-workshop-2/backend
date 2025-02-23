from datetime import datetime
from typing import NamedTuple


class RoutineModel(NamedTuple):
    id: str
    patient_id: str
    created_at: datetime
    updated_at: datetime
