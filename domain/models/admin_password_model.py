from datetime import datetime
from typing import NamedTuple


class AdminPasswordModel(NamedTuple):
    password: str
    created_at: datetime
    updated_at: datetime
