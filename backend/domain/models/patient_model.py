from datetime import datetime
from typing import NamedTuple


class PatientModel(NamedTuple):
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
