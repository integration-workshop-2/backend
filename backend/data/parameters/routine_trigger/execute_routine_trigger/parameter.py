from typing import NamedTuple


class RoutineTriggerArgsParameter(NamedTuple):
    patient_id: str
    medicine_id: str
    medicine_quantity: int
