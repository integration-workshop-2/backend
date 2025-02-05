from datetime import datetime
from typing import NamedTuple


class MedicineModel(NamedTuple):
    id: str
    name: str
    cylinder_number: int
    created_at: datetime
    updated_at: datetime
