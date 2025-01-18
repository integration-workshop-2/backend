from data.use_cases.medicine.create_medicine.use_case import CreateMedicineUseCase
from data.parameters.medicine.create_medicine.parameter import CreateMedicineParameter

from data.use_cases.medicine.list_available_cylinders.use_case import (
    ListAvailableCylindersUseCase,
)

from data.use_cases.medicine.delete_medicine.use_case import DeleteMedicineUseCase
from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter

if __name__ == "__main__":
    use_case = ListAvailableCylindersUseCase()
    print(use_case.execute())
