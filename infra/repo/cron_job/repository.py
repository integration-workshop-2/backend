from data.interfaces.cronjob_arguments_interface import CronJobArgumentsInterface
from datetime import datetime, timedelta, timezone
from domain.models.cronjob_model import CronJobModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List


class CronJobRepository(CronJobArgumentsInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_cronjob(self, execution_pattern: str, argument: str) -> CronJobModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO cron_job
            (execution_pattern, argument, created_at, updated_at)
            VALUES (%s, %s, %s, %s);
        """

        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (execution_pattern, argument, created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return CronJobModel(
            execution_pattern=execution_pattern,
            argument=argument,
            created_at=created_at,
            updated_at=updated_at,
        )

    def get_cronjob(self, execution_pattern: str) -> CronJobModel | None:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT execution_pattern, argument, created_at, updated_at
            FROM cron_job
            WHERE execution_pattern = %s;
        """

        values = (execution_pattern,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        if query_data:
            return CronJobModel(*query_data)

        return None

    def delete_cronjob(self, execution_pattern: str) -> CronJobModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_cronjob(execution_pattern=execution_pattern)

        query = """
            DELETE FROM cron_job
            WHERE execution_pattern = %s;
        """

        values = (execution_pattern,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return CronJobModel(
            execution_pattern=execution_pattern,
            argument=entity_instance.argument,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def list_cronjobs(self) -> List[CronJobModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT execution_pattern, argument, created_at, updated_at
            FROM cron_job;
        """

        cursor.execute(
            query,
        )
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        cron_jobs_model_list: List[CronJobModel] = []
        for query_data_item in query_data:
            model = CronJobModel(*query_data_item)
            cron_jobs_model_list.append(model)

        return cron_jobs_model_list

    def update_cronjob(self, execution_pattern: str, argument: str) -> CronJobModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_cronjob(execution_pattern=execution_pattern)

        query = """
            UPDATE cron_job
            SET execution_pattern = %s,
            argument = %s,
            created_at = %s,
            updated_at = %s
            WHERE execution_pattern = %s;
        """

        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            execution_pattern,
            argument,
            entity_instance.created_at,
            updated_at,
            execution_pattern,
        )

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return CronJobModel(
            execution_pattern=execution_pattern,
            argument=argument,
            created_at=entity_instance.created_at,
            updated_at=updated_at,
        )
