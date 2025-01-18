from data.parameters.medicine.create_medicine import CreateMedicineParameter
from infra.repo.medicine_repository.repository import MedicineRepository
from typing import Dict


class CreateMedicineUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self, parameter: CreateMedicineParameter) -> Dict:
        created_medicine = self.__medicine_repository.create_medicine(
            name=parameter.name, cylinder_number=parameter.cylinder_number
        )

        return {"success": True, "data": created_medicine._asdict()}
