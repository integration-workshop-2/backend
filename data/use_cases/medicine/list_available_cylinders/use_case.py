from infra.repo.medicine_repository.repository import MedicineRepository
from typing import Dict


class ListAvailableCylindersUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self) -> Dict:
        medicine_list = self.__medicine_repository.list_medicine()

        available_cylinders = [1, 2, 3]

        for medicine in medicine_list:
            available_cylinders.remove(medicine.cylinder_number)

        return {"success": True, "data": {"available_cylinders": available_cylinders}}
