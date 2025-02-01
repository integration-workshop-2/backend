from crontab import CronItem, CronTab
from datetime import time
from domain.models.cronjob_argument_model import (
    CronJobArgumentModel,
    CronJobMedicineDataModel,
)
from json import dumps, loads
from typing import Dict, List


class CrontabUtil:
    def __init__(self) -> None:
        self.__cron = CronTab(user=True)

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
            existent_routine_info_list = (
                self.__transform_list_dict_to_cron_job_argument_model_list(
                    routine_list=loads(job.comment)
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

                    job.command = f"/home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --routines_list {dumps(parsed_existent_routine_info_list)}"

                    job.set_comment(dumps(parsed_existent_routine_info_list))

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

            job.command = f"/home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --routines_list {dumps(parsed_existent_routine_info_list)}"

            job.set_comment(dumps(parsed_existent_routine_info_list))

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

            job_command = f"/home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --routines_list {parsed_existent_routine_info_list}"

            execution_pattern = f"{str(day_time.minute)} {str(day_time.hour)} * * {self.__get_week_day_number(week_day=week_day)}"

            job = self.__cron.new(
                command=job_command, comment=dumps(parsed_existent_routine_info_list)
            )
            job.setall(execution_pattern)
            self.__cron.write()

    def delete_routine_job_by_routine_id(self, routine_id: str) -> None:
        for job in self.__cron:
            routine_info_list: List[CronJobArgumentModel] = loads(job.comment)

            for routine_info in routine_info_list:
                if routine_info.routine_id == routine_id:
                    routine_info_list.remove(routine_info)

            if not routine_info_list:
                self.__cron.remove(job)

        self.__cron.write()

    def delete_routine_job_by_medicine_id(self, medicine_id: str) -> None:
        for job in self.__cron:
            comment = f"medicine_id={medicine_id}"
            if comment in job.comment:
                self.__cron.remove(job)

        self.__cron.write()

    def delete_routine_job_by_patient_id(self, patient_id: str) -> None:
        for job in self.__cron:
            comment = f"patient_id={patient_id}"
            if comment in job.comment:
                self.__cron.remove(job)

        self.__cron.write()
