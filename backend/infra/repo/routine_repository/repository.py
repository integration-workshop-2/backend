from data.interfaces.routine_interface import RoutineInterface
from datetime import datetime, timedelta, timezone
from domain.models.routine_model import RoutineModel
from infra.config.db_connection_handler import DBConnectionHandler
from uuid import uuid4


class RoutineRepository(RoutineInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_routine(self, patient_id: str) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO routine
            (id, patient_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            id,
            patient_id,
            created_at,
            updated_at,
        )

        cursor.execute(query, values)

        db_connection.commit()

        cursor.close()
        db_connection.close()

        return RoutineModel(
            id=id,
            patient_id=patient_id,
            created_at=created_at,
            updated_at=updated_at,
        )

    def delete_routine(self, id: str) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_routine(id=id)

        query = """
            DELETE FROM routine
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return RoutineModel(
            id=id,
            patient_id=entity_instance.patient_id,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def get_routine(self, id: str) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, created_at, updated_at
            FROM routine
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return RoutineModel(*query_data)
