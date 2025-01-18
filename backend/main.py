from data.use_cases.patient.update_patient import (
    UpdatePatientUseCase,
)
from data.parameters.patient.update_patient import (
    UpdatePatientParameter,
)

if __name__ == "__main__":
    use_case = UpdatePatientUseCase()
    parameter = UpdatePatientParameter(
        patient_id="9d5fdde4-c876-41e6-898e-615a595facc3",
        name="joao h",
    )
    print(use_case.execute(parameter=parameter))
