from data.interfaces.patient_faces_interface import PatientFacesInterface
from datetime import datetime, timedelta, timezone
from domain.models.patient_faces_model import PatientFacesModel
from infra.config.db_connection_handler import DBConnectionHandler
from json import dumps, loads
from typing import List
from uuid import uuid4


class PatientFacesRepository(PatientFacesInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_patient_faces(
        self, patient_id: str, face_embedding: List[float]
    ) -> PatientFacesModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO patient_faces
            (id, patient_id, face_embedding, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, patient_id, dumps(face_embedding), created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return PatientFacesModel(
            id=id,
            patient_id=patient_id,
            face_embedding=face_embedding,
            created_at=created_at,
            updated_at=updated_at,
        )

    def list_patient_faces_by_patient_id(
        self, patient_id: str
    ) -> List[PatientFacesModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, face_embedding, created_at, updated_at
            FROM patient_faces
            WHERE patient_id = %s;
        """

        values = (patient_id,)

        cursor.execute(query, values)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        patient_faces_model_list: List[PatientFacesModel] = []
        for query_data_item in query_data:
            id, patient_id, face_embedding, created_at, updated_at = query_data_item
            model = PatientFacesModel(
                id=id,
                patient_id=patient_id,
                face_embedding=loads(face_embedding),
                created_at=created_at,
                updated_at=updated_at,
            )
            patient_faces_model_list.append(model)

        return patient_faces_model_list
