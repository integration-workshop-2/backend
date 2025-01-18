from data.use_cases.patient.create_patient import CreatePatientUseCase
from data.parameters.patient.create_patient import CreatePatientParameter
from data.use_cases.patient.delete_patient import DeletePatientUseCase
from data.parameters.patient.delete_patient import DeletePatientParameter
from data.use_cases.patient.get_patient import GetPatientUseCase
from data.parameters.patient.get_patient import GetPatientParameter
from data.use_cases.patient.list_patients import ListPatientsUseCase
from data.parameters.patient.list_patients import ListPatientsParameter
from data.use_cases.patient.update_patient import UpdatePatientUseCase
from data.parameters.patient.update_patient import UpdatePatientParameter

from data.use_cases.non_recognized_patients.create_non_recognized_patient.use_case import (
    CreateNonRecognizedPatientUseCase,
)
from data.parameters.non_recognized_patients.create_non_recognized_patient import (
    CreateNonRecognizedPatientParameter,
)
from data.use_cases.non_recognized_patients.list_non_recognized_patients.use_case import (
    ListNonRecognizedPatientsUseCase,
)

if __name__ == "__main__":
    # create
    # use_case = CreatePatientUseCase()
    # parameter = CreatePatientParameter(
    #     name="pedro", face_embeddings=[[1.1, 2.2], [3.3, 4.4]]
    # )
    # print(use_case.execute(parameter=parameter))

    # list_patients_use_case = ListPatientsUseCase()
    # list_patients_parameter = ListPatientsParameter(patient_name="pa")
    # print(list_patients_use_case.execute(parameter=list_patients_parameter))

    # get_patient_use_case = GetPatientUseCase()
    # get_patient_parameter = GetPatientParameter(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f"
    # )
    # print(get_patient_use_case.execute(parameter=get_patient_parameter))

    use_case = CreateNonRecognizedPatientUseCase()
    parameter = CreateNonRecognizedPatientParameter(
        patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f"
    )
    print(use_case.execute(parameter=parameter))

    use_case = ListNonRecognizedPatientsUseCase()
    print(use_case.execute())
