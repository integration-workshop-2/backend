from data.interfaces import AdminPasswordInterface
from datetime import datetime, timedelta, timezone
from domain.models.admin_password_model import AdminPasswordModel
from infra.config.db_connection_handler import DBConnectionHandler


class AdminPasswordRepository(AdminPasswordInterface):
    __db_connection: DBConnectionHandler = None

    @classmethod
    def db_connection_instace(cls):
        if not cls.__db_connection:
            cls.__db_connection = DBConnectionHandler()

        return cls.__db_connection

    def get_admin_password(self) -> AdminPasswordModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        query = """
            SELECT password, created_at, updated_at
            FROM  admin_password;
        """

        cursor.execute(query)
        query_data = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return AdminPasswordModel(*query_data)

    def update_admin_password(self, password: str) -> AdminPasswordModel:
        db_connection = self.db_connection_instace().get_connection()
        cursor = db_connection.cursor()

        entity_instance = self.get_admin_password()

        query = """
            UPDATE admin_password
            SET  password = %s,
            created_at = %s,
            updated_at = %s;
        """

        updated_at = datetime.now(timezone.utc) - timedelta(hours=3)

        values = (password, entity_instance.created_at, updated_at)

        cursor.execute(query, values)
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return AdminPasswordModel(
            password=password,
            created_at=entity_instance.created_at,
            updated_at=updated_at,
        )
