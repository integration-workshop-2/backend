from data.interfaces.non_recognized_patients_interface import (
    NonRecognizedPatientsInterface,
)
from datetime import datetime, timedelta, timezone
from domain.models.non_recognized_patients_model import NonRecognizedPatientsModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List
from uuid import uuid4


class NonRecognizedPatientsRepository(NonRecognizedPatientsInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_non_recognized_patient(
        self, patient_id: str
    ) -> NonRecognizedPatientsModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO non_recognized_patients
            (id, patient_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, patient_id, created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return NonRecognizedPatientsModel(
            id=id,
            patient_id=patient_id,
            created_at=created_at,
            updated_at=updated_at,
        )

    def get_non_recognized_patient(self, id: str) -> NonRecognizedPatientsModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, created_at, updated_at
            FROM non_recognized_patients
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return NonRecognizedPatientsModel(*query_data)

    def list_non_recognized_patient(self) -> List[NonRecognizedPatientsModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, created_at, updated_at
            FROM non_recognized_patients;
        """

        cursor.execute(query)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        non_recognized_patients_model_list: List[NonRecognizedPatientsModel] = []
        for query_data_item in query_data:
            model = NonRecognizedPatientsModel(*query_data_item)
            non_recognized_patients_model_list.append(model)

        return non_recognized_patients_model_list
