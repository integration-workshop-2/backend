from data.parameters.routine_trigger.execute_routine_trigger.parameter import (
    RoutineTriggerArgsParameter,
)
from domain.models.cronjob_argument_model import CronJobArgumentModel
from infra.hardware.control_motor.control_motor import ControlMotor
from infra.repo.cron_job.repository import CronJobRepository
from infra.repo.medicine_repository.repository import MedicineRepository
from infra.repo.non_recognized_patients_repository.repository import (
    NonRecognizedPatientsRepository,
)
from infra.utils.browser_util.util import BrowserUtil
from json import loads
from typing import List


class ExecuteRoutineTriggerUseCase:
    def __init__(self) -> None:
        self.__browser_util = BrowserUtil()
        self.__cronjob_repository = CronJobRepository()
        self.__medicine_repository = MedicineRepository()
        self.__non_recognized_patients_repository = NonRecognizedPatientsRepository()

    def execute(self, parameter: RoutineTriggerArgsParameter) -> None:
        cronjob = self.__cronjob_repository.get_cronjob(
            execution_pattern=parameter.execution_pattern
        )

        routines_list: List[CronJobArgumentModel] = []

        for info in loads(cronjob.argument):
            routines_list.append(CronJobArgumentModel(**info))

        for patient_routine in routines_list:
            self.__browser_util.open_page(endpoint="index.html")

            response = None

            while not response:
                response = self.__browser_util.get_request_info(
                    endpoint="recognize_images"
                )

            if not response["success"]:
                self.__non_recognized_patients_repository.create_non_recognized_patient(
                    patient_id=patient_routine.patient_id
                )

            else:
                for medicine_info in patient_routine.medicine_data:

                    current_medicine = self.__medicine_repository.get_medicine(
                        id=medicine_info.medicine_id
                    )

                    cylinder_number = current_medicine.cylinder_number

                    control_motor = ControlMotor(cylinder_number=cylinder_number)

                    for _ in medicine_info.medicine_quantity:
                        control_motor.execute_controlled_movement()

            self.__browser_util.close_page()
