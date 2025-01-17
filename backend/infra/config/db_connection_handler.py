import mysql.connector


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__user = "eca"
        self.__password = "eca"
        self.__database = "eca"

    def get_connection(self) -> mysql.connector.MySQLConnection:
        return mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database,
        )
