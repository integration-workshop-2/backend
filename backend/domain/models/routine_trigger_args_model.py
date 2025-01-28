from typing import NamedTuple


class RoutineTriggerArgsModel(NamedTuple):
    patient_id: str
    medicine_id: str
    medicine_quantity: int
