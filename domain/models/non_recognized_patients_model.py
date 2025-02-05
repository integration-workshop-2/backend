from datetime import datetime
from typing import NamedTuple


class NonRecognizedPatientsModel(NamedTuple):
    id: str
    patient_id: str
    created_at: datetime
    updated_at: datetime
