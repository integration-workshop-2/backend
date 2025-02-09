from crontab import CronItem, CronTab
from datetime import time
from domain.models.cronjob_argument_model import (
    CronJobArgumentModel,
    CronJobMedicineDataModel,
)
from infra.repo.cron_job.repository import CronJobRepository
from json import dumps, loads
from typing import Dict, List


class CrontabUtil:
    def __init__(self) -> None:
        self.__cron = CronTab(user=True)
        self.__cronjob_repository = CronJobRepository()

    def __get_week_day_number(self, week_day: str) -> str:
        week_days = {
            "Sunday": "0",
            "Monday": "1",
            "Tuesday": "2",
            "Wednesday": "3",
            "Thursday": "4",
            "Friday": "5",
            "Saturday": "6",
        }

        return week_days[week_day]

    def __get_cronjob_by_execution_pattern(self, execution_pattern: str) -> CronItem:
        for job in self.__cron:
            if job.slices.render() == execution_pattern:
                return job

    def __check_execution_pattern_existency(
        self, week_day: str, day_time: time
    ) -> CronItem | None:
        for job in self.__cron:
            if (
                job.slices.render()
                == f"{str(day_time.minute)} {str(day_time.hour)} * * {self.__get_week_day_number(week_day=week_day)}"
            ):
                return job

        return None

    def __transform_list_dict_to_cron_job_argument_model_list(
        self, routine_list: List[Dict]
    ) -> List[CronJobArgumentModel]:
        cron_job_argument_model_list: List[CronJobArgumentModel] = []

        for routine_info in routine_list:
            cron_job_medicine_data_model_list: List[CronJobMedicineDataModel] = []

            for medicine_info in routine_info["medicine_data"]:
                cron_job_medicine_data_model_list.append(
                    CronJobMedicineDataModel(**medicine_info)
                )

            routine_info["medicine_data"] = cron_job_medicine_data_model_list
            cron_job_argument_model_list.append(CronJobArgumentModel(**routine_info))

        return cron_job_argument_model_list

    def __transform_cron_job_argument_model_list_to_list_dict(
        self, cron_job_argument_model_list: List[CronJobArgumentModel]
    ) -> List[Dict]:
        list_dict: List[Dict] = []

        for routine_info in cron_job_argument_model_list:
            medicine_data_list = []

            for medicine_data in routine_info.medicine_data:
                medicine_data_list.append(medicine_data._asdict())

            list_dict.append(
                {
                    "patient_id": routine_info.patient_id,
                    "routine_id": routine_info.routine_id,
                    "medicine_data": medicine_data_list,
                }
            )

        return list_dict

    def create_routine_job(
        self,
        routine_id: str,
        medicine_id: str,
        patient_id: str,
        medicine_quantity: int,
        week_day: str,
        day_time: time,
    ) -> None:

        # Checking if there is an existing job with the same execution pattern
        job = self.__check_execution_pattern_existency(
            week_day=week_day, day_time=day_time
        )

        if job:
            cronjob_model = self.__cronjob_repository.get_cronjob(
                execution_pattern=job.slices.render()
            )

            existent_routine_info_list = (
                self.__transform_list_dict_to_cron_job_argument_model_list(
                    routine_list=loads(cronjob_model.argument)
                )
            )

            for existent_routine_info in existent_routine_info_list:
                # If the patient already has a routine executing at this execution pattern,
                # simply add the new_medicine info at his/her info
                if existent_routine_info.patient_id == patient_id:
                    existent_routine_info.medicine_data.append(
                        CronJobMedicineDataModel(
                            medicine_id=medicine_id, medicine_quantity=medicine_quantity
                        )
                    )

                    parsed_existent_routine_info_list = (
                        self.__transform_cron_job_argument_model_list_to_list_dict(
                            cron_job_argument_model_list=existent_routine_info_list
                        )
                    )

                    self.__cronjob_repository.update_cronjob(
                        execution_pattern=job.slices.render(),
                        argument=dumps(parsed_existent_routine_info_list),
                    )

                    job.command = f'DISPLAY=:0 /home/jhcsoares/utfpr/integration_workshop_2/backend/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/backend/execute_routine_trigger.py --execution_pattern "{job.slices.render()}"'

                    job.set_comment(job.slices.render())

                    self.__cron.write()

                    return

            # If the patient does not have a routine executing at this execution pattern,
            # add a new CronJobArgumentModel to existent_routine_info_list
            existent_routine_info_list.append(
                CronJobArgumentModel(
                    patient_id=patient_id,
                    routine_id=routine_id,
                    medicine_data=[
                        CronJobMedicineDataModel(
                            medicine_id=medicine_id, medicine_quantity=medicine_quantity
                        )
                    ],
                )
            )

            parsed_existent_routine_info_list = (
                self.__transform_cron_job_argument_model_list_to_list_dict(
                    cron_job_argument_model_list=existent_routine_info_list
                )
            )

            self.__cronjob_repository.update_cronjob(
                execution_pattern=job.slices.render(),
                argument=dumps(parsed_existent_routine_info_list),
            )

            job.command = f"DISPLAY=:0 /home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --routines_list {job.slices.render()}"

            job.set_comment(job.slices.render())

            self.__cron.write()

        else:
            parsed_existent_routine_info_list = (
                self.__transform_cron_job_argument_model_list_to_list_dict(
                    cron_job_argument_model_list=[
                        CronJobArgumentModel(
                            patient_id=patient_id,
                            routine_id=routine_id,
                            medicine_data=[
                                CronJobMedicineDataModel(
                                    medicine_id=medicine_id,
                                    medicine_quantity=medicine_quantity,
                                )
                            ],
                        )
                    ]
                )
            )

            execution_pattern = f"{str(day_time.minute)} {str(day_time.hour)} * * {self.__get_week_day_number(week_day=week_day)}"

            self.__cronjob_repository.create_cronjob(
                execution_pattern=execution_pattern,
                argument=dumps(parsed_existent_routine_info_list),
            )

            job_command = f"DISPLAY=:0 /home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --routines_list {execution_pattern}"

            job = self.__cron.new(command=job_command, comment=execution_pattern)
            job.setall(execution_pattern)
            self.__cron.write()

    def delete_routine_job_by_routine_id(self, routine_id: str) -> None:
        cron_jobs_list = self.__cronjob_repository.list_cronjobs()

        for cron_job in cron_jobs_list:
            argument = self.__transform_list_dict_to_cron_job_argument_model_list(
                loads(cron_job.argument)
            )

            for argument_data in argument[:]:
                if argument_data.routine_id == routine_id:
                    argument.remove(argument_data)

            if argument:
                parsed_argument = (
                    self.__transform_cron_job_argument_model_list_to_list_dict(
                        cron_job_argument_model_list=argument
                    )
                )
                self.__cronjob_repository.update_cronjob(
                    execution_pattern=cron_job.execution_pattern,
                    argument=dumps(parsed_argument),
                )

            else:
                self.__cronjob_repository.delete_cronjob(
                    execution_pattern=cron_job.execution_pattern
                )
                self.__cron.remove(
                    self.__get_cronjob_by_execution_pattern(
                        execution_pattern=cron_job.execution_pattern
                    )
                )

        self.__cron.write()

    def delete_routine_job_by_medicine_id(self, medicine_id: str) -> None:
        cron_jobs_list = self.__cronjob_repository.list_cronjobs()

        for cron_job in cron_jobs_list:
            argument = self.__transform_list_dict_to_cron_job_argument_model_list(
                loads(cron_job.argument)
            )

            for argument_data in argument[:]:
                for medicine_data in argument_data.medicine_data[:]:
                    if medicine_data.medicine_id == medicine_id:
                        argument_data.medicine_data.remove(medicine_data)

                if not argument_data.medicine_data:
                    argument.remove(argument_data)

            if argument:
                parsed_argument = (
                    self.__transform_cron_job_argument_model_list_to_list_dict(
                        cron_job_argument_model_list=argument
                    )
                )
                self.__cronjob_repository.update_cronjob(
                    execution_pattern=cron_job.execution_pattern,
                    argument=dumps(parsed_argument),
                )

            else:
                self.__cronjob_repository.delete_cronjob(
                    execution_pattern=cron_job.execution_pattern
                )
                self.__cron.remove(
                    self.__get_cronjob_by_execution_pattern(
                        execution_pattern=cron_job.execution_pattern
                    )
                )

        self.__cron.write()

    def delete_routine_job_by_patient_id(self, patient_id: str) -> None:
        cron_jobs_list = self.__cronjob_repository.list_cronjobs()

        for cron_job in cron_jobs_list:
            argument = self.__transform_list_dict_to_cron_job_argument_model_list(
                loads(cron_job.argument)
            )

            for argument_data in argument[:]:
                if argument_data.patient_id == patient_id:
                    argument.remove(argument_data)

            if argument:
                parsed_argument = (
                    self.__transform_cron_job_argument_model_list_to_list_dict(
                        cron_job_argument_model_list=argument
                    )
                )
                self.__cronjob_repository.update_cronjob(
                    execution_pattern=cron_job.execution_pattern,
                    argument=dumps(parsed_argument),
                )

            else:
                self.__cronjob_repository.delete_cronjob(
                    execution_pattern=cron_job.execution_pattern
                )
                self.__cron.remove(
                    self.__get_cronjob_by_execution_pattern(
                        execution_pattern=cron_job.execution_pattern
                    )
                )

        self.__cron.write()
