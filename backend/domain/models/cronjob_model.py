from datetime import datetime
from typing import NamedTuple


class CronJobModel(NamedTuple):
    execution_pattern: str
    argument: str
    created_at: datetime
    updated_at: datetime
