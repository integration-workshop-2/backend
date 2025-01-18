from typing import NamedTuple, Optional


class ListPatientsParameter(NamedTuple):
    patient_name: Optional[str] = None
