from data.use_cases.patients_vital_signs.create_patient_vital_signs.use_case import (
    CreatePatientVitalSignsUseCase,
)
from data.parameters.patients_vital_signs.create_patient_vital_signs.parameter import (
    CreatePatientVitalSignsParameter,
)

from data.use_cases.patients_vital_signs.get_patient_vital_signs.use_case import (
    GetPatientVitalSignsUseCase,
)
from data.parameters.patients_vital_signs.get_patient_vital_signs.parameter import (
    GetPatientVitalSignsParameter,
)

if __name__ == "__main__":
    # use_case = CreatePatientVitalSignsUseCase()
    # parameter = CreatePatientVitalSignsParameter(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     bpm=100,
    #     oxygenation_percentage=98,
    # )
    # print(use_case.execute(parameter=parameter))

    use_case = GetPatientVitalSignsUseCase()
    parameter = GetPatientVitalSignsParameter(id="00756fd5-fb43-4b3d-b725-1507bcccd4bc")
    print(use_case.execute(parameter=parameter))
