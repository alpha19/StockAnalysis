import sqlite3
import os

__author__ = 'kdedow'

class Database(object):
    """
    Holds a connection to a database
    """

    def __init__(self, path: str):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        self.connnection = sqlite3.connect(self.path)

    def __enter__(self):
        # Open the conection
        return self

    def __exit__(self):
        # Close the connection
        self.connnection.commit()
        self.connnection.close()

    def close(self):
        # Close the connection
        self.connnection.commit()
        self.connnection.close()

    def query(self, query: str):
        # Query the database and return the result
        return self.connnection.execute(query)
