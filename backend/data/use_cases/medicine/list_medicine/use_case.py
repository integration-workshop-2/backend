from infra.repo.medicine_repository.repository import MedicineRepository
from typing import Dict


class ListMedicineUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self) -> Dict:
        medicine_list = self.__medicine_repository.list_medicine()

        data_list = []
        for medicine in medicine_list:
            parsed_medicine = medicine._asdict()
            data_list.append(parsed_medicine)

        return {"success": True, "data": data_list}
