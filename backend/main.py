from data.use_cases.patient.delete_patient import (
    DeletePatientUseCase,
)
from data.parameters.patient.delete_patient import (
    DeletePatientParameter,
)

if __name__ == "__main__":
    use_case = DeletePatientUseCase()
    parameter = DeletePatientParameter(
        patient_id="9d5fdde4-c876-41e6-898e-615a595facc3"
    )
    print(use_case.execute(parameter=parameter))
