from datetime import datetime
from typing import List, NamedTuple


class PatientFacesModel(NamedTuple):
    id: str
    patient_id: str
    face_embedding: List[float]
    created_at: datetime
    updated_at: datetime
