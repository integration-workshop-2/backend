from data.use_cases.medicine.create_medicine.use_case import CreateMedicineUseCase
from data.parameters.medicine.create_medicine.parameter import CreateMedicineParameter

from data.use_cases.medicine.delete_medicine.use_case import DeleteMedicineUseCase
from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter

if __name__ == "__main__":
    use_case = DeleteMedicineUseCase()
    parameter = DeleteMedicineParameter(
        medicine_id="238b99f7-933c-4a92-aece-7187b202a59c"
    )
    print(use_case.execute(parameter=parameter))
