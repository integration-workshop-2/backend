from typing import List, NamedTuple


class CronJobMedicineDataModel(NamedTuple):
    medicine_id: str
    medicine_quantity: int


class CronJobArgumentModel(NamedTuple):
    patient_id: str
    routine_id: str
    medicine_data: List[CronJobMedicineDataModel]
