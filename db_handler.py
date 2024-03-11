import create_db
import sqlite3
from sqlite3 import Error
import sys
import create_db

connection = None


def create_connection():
    global connection

    try:
        connection = sqlite3.connect("order_system.db")
        create_db.initialize_tables(connection)
    except Error as e:
        sys.exit("DB Error: " + str(e))


create_connection()


class DB_Handler:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DB_Handler, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def get_connection(cls):
        return connection

    @classmethod
    def close_connection(cls):
        if connection:
            connection.close()
