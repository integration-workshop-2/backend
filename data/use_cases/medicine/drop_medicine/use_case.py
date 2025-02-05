from data.parameters.medicine.drop_medicine.parameter import DropMedicineParameter
from infra.repo.medicine_repository.repository import MedicineRepository
from infra.hardware.control_motor.control_motor import ControlMotor
from typing import Dict, List


class DropMedicineUseCase:
    def __init__(self) -> None:
        self.__medicine_repository = MedicineRepository()

    def execute(self, parameter: DropMedicineParameter) -> Dict:
        for _ in range(parameter.medicine_quantity):
            cylinder_number = self.__medicine_repository.get_medicine(
                id=parameter.medicine_id
            ).cylinder_number

            self.__control_motor.execute_controlled_movement()

        return {"success": True}

    def __get_motor_bus_by_cylinder_number(self, cylinder_number: int) -> List[int]:
        motor_bus = {
            1: [1, 2, 3, 4],
            2: [5, 6, 7, 8],
            3: [9, 10, 11, 12],
        }

        return motor_bus[cylinder_number]
