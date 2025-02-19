import requests

from data.parameters.routine_trigger.execute_routine_trigger.parameter import (
    RoutineTriggerArgsParameter,
)
from domain.models.cronjob_argument_model import CronJobArgumentModel
from infra.repo.alarms_repository.repository import AlarmsRepository
from infra.repo.cron_job.repository import CronJobRepository
from infra.repo.medicine_repository.repository import MedicineRepository
from infra.repo.non_recognized_patients_repository.repository import (
    NonRecognizedPatientsRepository,
)
from infra.repo.patient_repository.repository import PatientRepository
from infra.repo.patients_vital_signs_repository.repository import (
    PatientsVitalSignsRepository,
)
from infra.utils.browser_util.util import BrowserUtil
from infra.utils.speaker_util.util import SpeakerUtil
from json import loads
from typing import List


class ExecuteRoutineTriggerUseCase:
    def __init__(self) -> None:
        self.__alarms_repository = AlarmsRepository()
        self.__browser_util = BrowserUtil()
        self.__cronjob_repository = CronJobRepository()
        self.__medicine_repository = MedicineRepository()
        self.__non_recognized_patients_repository = NonRecognizedPatientsRepository()
        self.__patient_repository = PatientRepository()
        self.__patients_vital_signs_repository = PatientsVitalSignsRepository()
        self.__speaker_util = SpeakerUtil()

    def execute(self, parameter: RoutineTriggerArgsParameter) -> None:
        cronjob = self.__cronjob_repository.get_cronjob(
            execution_pattern=parameter.execution_pattern
        )

        routines_list: List[CronJobArgumentModel] = []

        for info in loads(cronjob.argument):
            routines_list.append(CronJobArgumentModel(**info))

        for patient_routine in routines_list:
            self.__browser_util.open_page(endpoint="index.html")

            patient_name = self.__patient_repository.get_patient(
                id=patient_routine.patient_id
            ).name

            self.__speaker_util.speak(f"Paciente {patient_name}")

            for _ in range(5):
                requests.get(url="http://10.42.0.2/capture")

            response = requests.get(
                url=f"http://10.42.0.1:5000/api/recognize_images/{patient_routine.patient_id}"
            ).json()

            if not response["success"]:
                self.__speaker_util.speak("Paciente não reconhecido")

                self.__non_recognized_patients_repository.create_non_recognized_patient(
                    patient_id=patient_routine.patient_id
                )

            else:
                self.__speaker_util.speak(
                    "Paciente reconhecido. Insira os dedos nos sensores de sinais vitais"
                )

                i = 0
                while i <= 4:
                    response = requests.get(
                        url="http://10.42.0.3:5000/api/vital_signs_sensors"
                    ).json()

                    if response["success"]:
                        bpm = response["data"]["bpm"]
                        oxygenation_percentage = response["data"][
                            "oxygenation_percentage"
                        ]
                        temperature = response["data"]["temperature"]

                        created_patient_vital_signs = self.__patients_vital_signs_repository.create_patient_vital_signs(
                            patient_id=patient_routine.patient_id,
                            bpm=bpm,
                            oxygenation_percentage=oxygenation_percentage,
                            temperature=temperature,
                        )

                        if bpm < 40 or bpm > 160:
                            self.__alarms_repository.create_alarm(
                                patient_vital_signs_id=created_patient_vital_signs.id
                            )

                        elif oxygenation_percentage < 80:
                            self.__alarms_repository.create_alarm(
                                patient_vital_signs_id=created_patient_vital_signs.id
                            )

                        elif temperature < 20 or temperature > 40:
                            self.__alarms_repository.create_alarm(
                                patient_vital_signs_id=created_patient_vital_signs.id
                            )

                        i += 1

                self.__speaker_util.speak(
                    "Leitura concluída. Aguarde o comando para pegar os remédios"
                )

                for medicine_info in patient_routine.medicine_data:
                    current_medicine = self.__medicine_repository.get_medicine(
                        id=medicine_info["medicine_id"]
                    )

                    cylinder_number = current_medicine.cylinder_number

                    for _ in range(medicine_info["medicine_quantity"]):
                        requests.get(
                            url=f"http://10.42.0.3:5000/api/control_motor/{cylinder_number}"
                        )

                self.__speaker_util.speak("Remédios na bandeja")

            self.__browser_util.close_page()
