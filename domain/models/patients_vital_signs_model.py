from datetime import datetime
from typing import NamedTuple


class PatientsVitalSignsModel(NamedTuple):
    id: str
    patient_id: str
    bpm: int
    oxygenation_percentage: int
    created_at: datetime
    updated_at: datetime
