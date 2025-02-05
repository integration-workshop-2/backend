from data.interfaces.patient_interface import PatientInterface
from datetime import datetime, timedelta, timezone
from domain.models.patient_model import PatientModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List
from uuid import uuid4


class PatientRepository(PatientInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_patient(self, name: str) -> PatientModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO patient
            (id, name, created_at, updated_at)
            VALUES (%s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, name, created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return PatientModel(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

    def delete_patient(self, id: str) -> PatientModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_patient(id=id)

        query = """
            DELETE FROM patient
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return PatientModel(
            id=id,
            name=entity_instance.name,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def get_patient(self, id: str) -> PatientModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, name, created_at, updated_at
            FROM patient
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return PatientModel(*query_data)

    def list_patients(self, name: str = "") -> List[PatientModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        if not name:
            query = """
                SELECT id, name, created_at, updated_at
                FROM patient;
            """
            values = None

        else:
            name = f"%{name}%"
            query = """
                SELECT id, name, created_at, updated_at
                FROM patient
                WHERE name LIKE %s;
            """
            values = (name,)

        cursor.execute(query, values)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        patient_model_list: List[PatientModel] = []
        for query_data_item in query_data:
            model = PatientModel(*query_data_item)
            patient_model_list.append(model)

        return patient_model_list

    def update_patient(self, id: str, name: str) -> PatientModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_patient(id=id)

        query = """
            UPDATE patient
            SET id = %s,
            name = %s,
            created_at = %s,
            updated_at = %s
            WHERE id = %s;
        """

        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, name, entity_instance.created_at, updated_at, id)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return PatientModel(
            id=id,
            name=name,
            created_at=entity_instance.created_at,
            updated_at=updated_at,
        )
