from typing import NamedTuple


class CreatePatientVitalSignsParameter(NamedTuple):
    patient_id: str
    bpm: int
    oxygenation_percentage: int
