"""
    Models that handles the business/algorithmic logic for the string search functionality
"""
from general.databases.MongoDBHandler import MongoDBHandler
import os
import logging

logger = logging.getLogger(__name__)

SEARCH_DATABASE = os.getenv('SEARCH_STRING_DB')
SEARCH_COLLECTION = os.getenv("SEARCH_STRING_COL")


def search_string_model(search_string):
    """
    Does a search on the Mongo database of the search_string
    :param search_string: The string to be searched
    :return: The result object.
    """
    mongo_client = MongoDBHandler()
    connection = mongo_client.get_connection()
    print(SEARCH_DATABASE)
    db = connection.get_database(SEARCH_DATABASE)
    collection = db.get_collection(SEARCH_COLLECTION)
    search_result = collection.find({"text": search_string})
    result = [matched_string for matched_string in search_result]
    if result:
        return result[0].get('text')
    else:
        return None

