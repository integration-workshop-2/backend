import fcntl
import os

from data.parameters.routine_trigger.execute_routine_trigger.parameter import (
    RoutineTriggerArgsParameter,
)
from infra.repo.non_recognized_patients_repository.repository import (
    NonRecognizedPatientsRepository,
)
from infra.utils.browser_util.util import BrowserUtil


class ExecuteRoutineTriggerUseCase:
    def __init__(self) -> None:
        self.__non_recognized_patients_repository = NonRecognizedPatientsRepository()
        self.__browser_util = BrowserUtil()
        self.__lock_file_path = (
            "/home/jhcsoares/utfpr/integration_workshop_2/patient.lock"
        )

    def execute(self, parameter: RoutineTriggerArgsParameter) -> None:
        self.__patient_id = parameter.patient_id
        self.__medicine_id = parameter.medicine_id
        self.__medicine_quantity = parameter.medicine_quantity

        if not os.path.exists(self.__lock_file_path):
            self.__create_lock_file()
            self.__execute_routine()

        else:
            pass

    def __create_lock_file(self) -> None:
        with open(self.__lock_file_path, "w") as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            file.write(f"{self.__patient_id}")
            file.flush()

    def __execute_routine(self) -> None:
        self.__browser_util.open_page("index.html")

        response = None

        while not response:
            response = self.__browser_util.get_request_info(endpoint="recognize_images")

        if not response["success"]:
            self.__non_recognized_patients_repository.create_non_recognized_patient(
                patient_id=self.__patient_id
            )

        else:
            pass

        self.__browser_util.close_page()
        os.remove(self.__lock_file_path)
