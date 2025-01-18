from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter
from infra.repo.medicine_repository.repository import MedicineRepository
from typing import Dict


class DeleteMedicineUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self, parameter: DeleteMedicineParameter) -> Dict:
        deleted_medicine = self.__medicine_repository.delete_medicine(
            id=parameter.medicine_id
        )

        return {"success": True, "data": deleted_medicine._asdict()}
