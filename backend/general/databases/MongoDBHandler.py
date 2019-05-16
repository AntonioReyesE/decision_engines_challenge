"""
    Database configuration and setup for MongoDB
"""
from general.Singleton import Singleton
from pymongo import MongoClient
import logging
import os

SECRETS_MONGO_URI = os.environ.get("MONGO_URI")


class MongoDBHandler(metaclass=Singleton):
    """
    Class that handles the Mongo database connection as a Singleton.
    """

    def __init__(self):
        self._conn = None
        self.mongo_uri = SECRETS_MONGO_URI
        self.logger = logging.getLogger(__name__)

    def init_db(self):
        """
        Initializes the database connection
        """
        self._conn = self.get_connection()

    def get_connection(self):
        """
        Gets the single connection
        :return: A pymongo MongoClient connection.
        """
        if not self._conn:
            self.logger.info("Creating new mongo database connection")
            self._conn = MongoClient(self.mongo_uri)
            return self._conn
        return self._conn

    def close(self):
        """
        Closes the unique database connection
        """
        if self._conn is not None:
            self._conn.close()
            self._conn = None