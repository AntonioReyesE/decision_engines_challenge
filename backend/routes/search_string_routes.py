"""
    Define all the routes related to the search_string functionality.
"""

from controllers.search_string_controllers import search_string_controller
from flask import (
    Blueprint, Response, request
)

search_bp = Blueprint('search_string_routes', __name__, url_prefix='/')


@search_bp.route('/search', methods=['POST'])
def search_string():
    """
    Searches a given string in a Mongo Database.
    :return: The response with the result of the search.
    """
    text = request.json
    return search_string_controller(text)
