from typing import NamedTuple


class UpdateMedicineParameter(NamedTuple):
    medicine_id: str
    name: str
    cylinder_number: int
