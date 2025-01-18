from data.use_cases.medicine.create_medicine.use_case import CreateMedicineUseCase
from data.parameters.medicine.create_medicine.parameter import CreateMedicineParameter

from data.use_cases.medicine.update_medicine.use_case import UpdateMedicineUseCase
from data.parameters.medicine.update_medicine.parameter import UpdateMedicineParameter

from data.use_cases.medicine.list_available_cylinders.use_case import (
    ListAvailableCylindersUseCase,
)

from data.use_cases.medicine.delete_medicine.use_case import DeleteMedicineUseCase
from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter

if __name__ == "__main__":
    use_case = UpdateMedicineUseCase()
    parameter = UpdateMedicineParameter(
        medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
        name="paracetamol",
        cylinder_number=1,
    )
    print(use_case.execute(parameter=parameter))
