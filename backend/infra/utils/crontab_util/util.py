from crontab import CronTab
from datetime import time


class CrontabUtil:
    def create_routine_job(
        self,
        routine_id: str,
        cylinder_number: int,
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

        cron = CronTab(user=True)

        job_command = f"/home/jhcsoares/utfpr/integration_workshop_2/raspberrypi/.venv/bin/python /home/jhcsoares/utfpr/integration_workshop_2/test_routes.py {str(cylinder_number)} {str(medicine_quantity)}"

        execution_pattern = f"{str(day_time.minute)} {str(day_time.hour)} * * {get_week_day_number(week_day=week_day)}"

        job = cron.new(command=job_command, comment=routine_id)
        job.setall(execution_pattern)

        cron.write()
