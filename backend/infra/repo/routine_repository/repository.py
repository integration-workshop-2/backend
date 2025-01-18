from data.interfaces.routine_interface import RoutineInterface
from datetime import datetime, time, timedelta, timezone
from domain.models.routine_model import RoutineDataModel, RoutineModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List, Literal
from uuid import uuid4


class RoutineRepository(RoutineInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_routine(
        self,
        patient_id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: time,
    ) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO routine
            (id, patient_id, medicine_id, medicine_quantity, week_day, day_time, routine_description, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        id = str(uuid4())
        routine_description = 1
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            id,
            patient_id,
            medicine_id,
            medicine_quantity,
            week_day,
            day_time,
            routine_description,
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
            medicine_id=medicine_id,
            medicine_quantity=medicine_quantity,
            week_day=week_day,
            day_time=day_time,
            routine_description=routine_description,
            created_at=created_at,
            updated_at=updated_at,
        )

    def delete_routine_item(self, id: str) -> RoutineModel:
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
            medicine_id=entity_instance.medicine_id,
            medicine_quantity=entity_instance.medicine_id,
            week_day=entity_instance.week_day,
            day_time=entity_instance.day_time,
            routine_description=entity_instance.routine_description,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def delete_routine_by_patient_id(self, patient_id: str) -> List[RoutineModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instances = self.list_routines_by_patient_id(patient_id=patient_id)

        query = """
            DELETE FROM routine
            WHERE patient_id = %s;
        """

        values = (patient_id,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return entity_instances

    def get_routine(self, id: str) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, medicine_id, medicine_quantity, week_day, day_time, routine_description, created_at, updated_at
            FROM routine
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return RoutineModel(*query_data)

    def list_routines(
        self, patient_name: str = "", routine_description: str = ""
    ) -> List[RoutineDataModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT p.name, r.routine_description
            FROM routine r
            INNER JOIN patient p
            ON r.patient_id = p.id
        """

        values = []

        if patient_name:
            patient_name = f"%{patient_name}%"
            query += "WHERE p.name LIKE %s"
            values.append(patient_name)

        if routine_description:
            routine_description = f"%{routine_description}%"

            if values:
                query += "AND r.routine_description LIKE %s"

            else:
                query += "WHERE r.routine_description LIKE %s"

            values.append(routine_description)

        query += ";"

        cursor.execute(query, values)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        routine_data_model_list: List[RoutineDataModel] = []
        for query_data_item in query_data:
            model = RoutineDataModel(*query_data_item)
            routine_data_model_list.append(model)

        return routine_data_model_list

    def list_routines_by_patient_id(self, patient_id: str) -> List[RoutineModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, medicine_id, medicine_quantity, week_day, day_time, routine_description, created_at, updated_at
            FROM routine
            WHERE patient_id = %s;
        """

        values = (patient_id,)

        cursor.execute(query, values)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        routine_data_model_list: List[RoutineModel] = []
        for query_data_item in query_data:
            model = RoutineModel(*query_data_item)
            routine_data_model_list.append(model)

        return routine_data_model_list

    def update_routine(
        self,
        id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: datetime,
    ) -> RoutineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_routine(id=id)

        query = """
            UPDATE routine
            SET id = %s,
            medicine_id = %s,
            medicine_quantity = %s,
            week_day = %s,
            day_time = %s,
            routine_description = %s,
            created_at = %s,
            updated_at = %s
            WHERE id = %s;
        """

        routine_description = 1
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            id,
            medicine_id,
            medicine_quantity,
            week_day,
            day_time,
            routine_description,
            entity_instance.created_at,
            updated_at,
            id,
        )

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return RoutineModel(
            id=id,
            patient_id=entity_instance.patient_id,
            medicine_id=medicine_id,
            medicine_quantity=medicine_quantity,
            week_day=week_day,
            day_time=day_time,
            routine_description=routine_description,
            created_at=entity_instance.created_at,
            updated_at=updated_at,
        )
