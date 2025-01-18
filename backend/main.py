from data.use_cases.patient.create_patient import (
    CreatePatientUseCase,
)
from data.parameters.patient.create_patient import (
    CreatePatientParameter,
)

if __name__ == "__main__":
    use_case = CreatePatientUseCase()
    parameter = CreatePatientParameter(
        name="joao", face_embeddings=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    )
    print(use_case.execute(parameter=parameter))
