from typing import NamedTuple, Optional


class ListRoutinesParameter(NamedTuple):
    patient_name: Optional[str] = None
    routine_description: Optional[str] = None
