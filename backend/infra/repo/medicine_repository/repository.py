from data.interfaces.medicine_interface import MedicineInterface
from datetime import datetime, timedelta, timezone
from domain.models.medicine_model import MedicineModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List
from uuid import uuid4


class MedicineRepository(MedicineInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_medicine(self, name: str, cylinder_number: int) -> MedicineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO medicine
            (id, name, cylinder_number, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s);
        """

        id = str(uuid4())
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, name, cylinder_number, created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return MedicineModel(
            id=id,
            name=name,
            cylinder_number=cylinder_number,
            created_at=created_at,
            updated_at=updated_at,
        )

    def delete_medicine(self, id: str) -> MedicineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_medicine(id=id)

        query = """
            DELETE FROM medicine
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return MedicineModel(
            id=id,
            name=entity_instance.name,
            cylinder_number=entity_instance.cylinder_number,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def get_medicine(self, id: str) -> MedicineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, name, cylinder_number, created_at, updated_at
            FROM medicine
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return MedicineModel(*query_data)

    def list_medicine(self) -> List[MedicineModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, name, cylinder_number, created_at, updated_at
            FROM medicine;
        """

        cursor.execute(query)
        query_data = cursor.fetchall()

        cursor.close()
        db_connection.close()

        medicine_model_list: List[MedicineModel] = []
        for query_data_item in query_data:
            model = MedicineModel(*query_data_item)
            medicine_model_list.append(model)

        return medicine_model_list

    def update_medicine(
        self, id: str, name: str, cylinder_number: int
    ) -> MedicineModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_medicine(id=id)

        query = """
            UPDATE medicine
            SET id = %s,
            name = %s,
            cylinder_number = %s,
            created_at = %s,
            updated_at = %s
            WHERE id = %s;
        """

        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (id, name, cylinder_number, entity_instance.created_at, updated_at, id)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return MedicineModel(
            id=id,
            name=name,
            cylinder_number=cylinder_number,
            created_at=entity_instance.created_at,
            updated_at=updated_at,
        )
