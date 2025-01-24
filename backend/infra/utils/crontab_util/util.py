from crontab import CronTab
from datetime import time


class CrontabUtil:
    def __init__(self) -> None:
        self.__cron = CronTab(user=True)

    def create_routine_job(
        self,
        routine_id: str,
        medicine_id: str,
        patient_id: str,
        medicine_quantity: int,
        week_day: str,
        day_time: time,
    ) -> None:
        def get_week_day_number(week_day: str) -> str:
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

        job_command = f"/home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py --medicine_id {medicine_id} --medicine_quantity {str(medicine_quantity)}"

        execution_pattern = f"{str(day_time.minute)} {str(day_time.hour)} * * {get_week_day_number(week_day=week_day)}"

        comment = (
            f"routine_id={routine_id} patient_id={patient_id} medicine_id={medicine_id}"
        )

        job = self.__cron.new(command=job_command, comment=comment)
        job.setall(execution_pattern)

        self.__cron.write()

    def delete_routine_job_by_routine_id(self, routine_id: str) -> None:
        for job in self.__cron:
            comment = f"routine_id={routine_id}"
            if comment in job.comment:
                self.__cron.remove(job)

        self.__cron.write()

    def delete_routine_job_by_medicine_id(self, medicine_id: str) -> None:
        for job in self.__cron:
            comment = f"medicine_id={medicine_id}"
            if comment in job.comment:
                self.__cron.remove(job)

    def delete_routine_job_by_patient_id(self, patient_id: str) -> None:
        for job in self.__cron:
            comment = f"patient_id={patient_id}"
            if comment in job.comment:
                self.__cron.remove(job)
