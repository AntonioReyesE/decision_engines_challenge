"""
    Controller for the search string functionality
"""

from flask import Response
from models.search_string_models import search_string_model
import json
import logging

logger = logging.getLogger(__name__)


def search_string_controller(search):
    """
    Controller that handles the route logic for the search string functionality
    :return: A Response object with the result of the search if found or an error message if not
    """
    response = Response()
    search_string = search.get('string_search')
    if search_string:
        logger.info("Searching string: {}".format(search))
        search_result = search_string_model(search_string)
        if search_result:
            response.data = json.dumps({'search_result': search_result})
            response.status_code = 200
        else:
            response.data = json.dumps({'msg': 'No string match found for {}'.format(search_string)})
            response.status_code = 404
        return response
    else:
        response.data = json.dumps({'msg': 'Empty request cannot be processed'})
        response.status_code = 404
        return response
