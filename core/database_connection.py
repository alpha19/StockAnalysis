import sqlite3
import os

__author__ = 'kdedow'

class Database(object):
    """
    Holds a connection to a database
    """

    def __init__(self, path: str):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

    def __enter__(self):
        # Open the conection
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection
        pass

    def close(self):
        # Close the connection
        pass

    def query(self, query: str, parameters=()):
        # Query the database with parameters and return the result
        connection = sqlite3.connect(self.path)
        result = connection.execute(query, parameters).fetchall()
        # Commit the result
        connection.commit()
        connection.close()

        return result
