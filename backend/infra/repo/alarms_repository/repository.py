from data.interfaces.alarms_interface import AlarmsInterface
from datetime import datetime, timedelta, timezone
from domain.models.alarms_model import AlarmsDataModel, AlarmsModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List
from uuid import uuid4


class AlarmsRepository(AlarmsInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_alarm(self, patient_vital_signs_id: str) -> AlarmsModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO alarms
            (id, patient_vital_signs_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, patient_vital_signs_id, created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return AlarmsModel(
            id=id,
            patients_vital_signs_id=patient_vital_signs_id,
            created_at=created_at,
            updated_at=updated_at,
        )

    def list_alarms(self) -> List[AlarmsModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT p.name as patient_name, pvs.bpm, pvs.oxygenation_percentage, a.created_at as date
            FROM alarms a
            INNER JOIN patients_vital_signs pvs
            ON a.patient_vital_signs_id = pvs.id
            INNER JOIN patient p
            ON pvs.patient_id = p.id;
        """

        cursor.execute(query)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        alarms_data_model_list: List[AlarmsDataModel] = []
        for query_data_item in query_data:
            model = AlarmsDataModel(*query_data_item)
            alarms_data_model_list.append(model)

        return alarms_data_model_list
