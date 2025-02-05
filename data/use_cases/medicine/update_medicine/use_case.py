from data.parameters.medicine.update_medicine.parameter import UpdateMedicineParameter
from infra.repo.medicine_repository.repository import MedicineRepository
from typing import Dict


class UpdateMedicineUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self, parameter: UpdateMedicineParameter) -> Dict:
        updated_medicine = self.__medicine_repository.update_medicine(
            id=parameter.medicine_id,
            name=parameter.name,
            cylinder_number=parameter.cylinder_number,
        )

        return {"success": True, "data": updated_medicine._asdict()}
