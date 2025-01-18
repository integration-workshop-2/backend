from data.use_cases.medicine.create_medicine.use_case import CreateMedicineUseCase
from data.parameters.medicine.create_medicine.parameter import CreateMedicineParameter

if __name__ == "__main__":
    use_case = CreateMedicineUseCase()
    parameter = CreateMedicineParameter(name="nimesulida", cylinder_number=1)
    print(use_case.execute(parameter=parameter))
