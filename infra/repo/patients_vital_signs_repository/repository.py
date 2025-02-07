from data.interfaces.patients_vital_signs_interface import PatientsVitalSignalsInterface
from datetime import datetime, timedelta, timezone
from domain.models.patients_vital_signs_model import PatientsVitalSignsModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List
from uuid import uuid4


class PatientsVitalSignsRepository(PatientsVitalSignalsInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_patient_vital_signs(
        self, patient_id: str, bpm: int, oxygenation_percentage: int, temperature: float
    ) -> PatientsVitalSignsModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO patients_vital_signs
            (id, patient_id, bpm, oxygenation_percentage, temperature, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            id,
            patient_id,
            bpm,
            oxygenation_percentage,
            temperature,
            created_at,
            updated_at,
        )

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return PatientsVitalSignsModel(
            id=id,
            patient_id=patient_id,
            bpm=bpm,
            oxygenation_percentage=oxygenation_percentage,
            temperature=temperature,
            created_at=created_at,
            updated_at=updated_at,
        )

    def get_patient_vital_signs(self, id: str) -> PatientsVitalSignsModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, bpm, oxygenation_percentage, created_at, updated_at
            FROM patients_vital_signs
            WHERE id = %s;
        """
        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return PatientsVitalSignsModel(*query_data)

    def list_patient_vital_signs(
        self, patient_id: str
    ) -> List[PatientsVitalSignsModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, patient_id, bpm, oxygenation_percentage, created_at, updated_at
            FROM patients_vital_signs
            WHERE patient_id = %s
            ORDER by created_at ASC;
        """
        values = (patient_id,)

        cursor.execute(query, values)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        patients_vital_signs_model_list: List[PatientsVitalSignsModel] = []
        for query_data_item in query_data:
            model = PatientsVitalSignsModel(*query_data_item)
            patients_vital_signs_model_list.append(model)

        return patients_vital_signs_model_list
