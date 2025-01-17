from datetime import datetime
from typing import NamedTuple


class AlarmsModel(NamedTuple):
    id: str
    patients_vital_signs_id: str
    created_at: datetime
    updated_at: datetime


class AlarmsDataModel(NamedTuple):
    patient_name: str
    bpm: int
    oxygenation_percentage: int
    date: datetime
