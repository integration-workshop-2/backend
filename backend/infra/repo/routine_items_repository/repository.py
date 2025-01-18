from data.interfaces.routine_items_interface import RoutineItemsInterface
from datetime import datetime, time, timedelta, timezone
from domain.models.medicine_model import MedicineModel
from domain.models.routine_item_model import RoutineItemDataModel, RoutineItemModel
from infra.config.db_connection_handler import DBConnectionHandler
from typing import List, Literal
from uuid import uuid4


class RoutineItemsRepository(RoutineItemsInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def create_routine_item(
        self,
        routine_id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: time,
    ) -> RoutineItemModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            INSERT INTO routine_items
            (id, 
            routine_id, 
            medicine_id, 
            medicine_quantity, 
            week_day, 
            day_time, 
            routine_description, 
            created_at, 
            updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        id = str(uuid4())
        routine_description = self.__get_routine_description(
            medicine_id=medicine_id,
            medicine_quantity=medicine_quantity,
            week_day=week_day,
            day_time=day_time,
        )
        created_at = datetime.now(timezone.utc) - timedelta(hours=3)
        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (
            id,
            routine_id,
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

        return RoutineItemModel(
            id=id,
            routine_id=routine_id,
            medicine_id=medicine_id,
            medicine_quantity=medicine_quantity,
            week_day=week_day,
            day_time=day_time,
            routine_description=routine_description,
            created_at=created_at,
            updated_at=updated_at,
        )

    def __get_routine_description(
        self,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: time,
    ) -> str:
        def __get_translated_week_day(week_day: str) -> str:
            week_days = {
                "Monday": "Seg",
                "Tuesday": "Ter",
                "Wednesday": "Qua",
                "Thursday": "Qui",
                "Friday": "Sex",
                "Saturday": "Sáb",
                "Sunday": "Dom",
            }

            return week_days[week_day]

        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, name, cylinder_number, created_at, updated_at
            FROM medicine
            WHERE id = %s;
        """

        values = (medicine_id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        medicine = MedicineModel(*query_data)
        translated_week_day = __get_translated_week_day(week_day=week_day)

        routine_description = f"{translated_week_day} {day_time.strftime("%H:%M")} {medicine.name} {medicine_quantity} comp."

        return routine_description

    def delete_routine_item(self, id: str) -> RoutineItemModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_routine_item(id=id)

        query = """
            DELETE FROM routine_items
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return RoutineItemModel(
            id=id,
            routine_id=entity_instance.routine_description,
            medicine_id=entity_instance.medicine_id,
            medicine_quantity=entity_instance.medicine_id,
            week_day=entity_instance.week_day,
            day_time=entity_instance.day_time,
            routine_description=entity_instance.routine_description,
            created_at=entity_instance.created_at,
            updated_at=entity_instance.updated_at,
        )

    def get_routine_item(self, id: str) -> RoutineItemModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT id, 
            routine_id, 
            medicine_id, 
            medicine_quantity, 
            week_day, 
            day_time, 
            routine_description, 
            created_at, 
            updated_at
            FROM routine_item
            WHERE id = %s;
        """

        values = (id,)

        cursor.execute(query, values)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return RoutineItemModel(*query_data)

    def list_routine_items(
        self,
        patient_name: str = "",
        routine_description: str = "",
    ) -> List[RoutineItemDataModel]:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT p.patient_name, ri.routine_description
            FROM routine_items ri
            INNER JOIN routine r
            ON ri.routine_id = r.id
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

        routine_item_data_model_list: List[RoutineItemModel] = []
        for query_data_item in query_data:
            routine_item_data_model = RoutineItemDataModel(*query_data_item)
            routine_item_data_model_list.append(routine_item_data_model)

        return routine_item_data_model_list
