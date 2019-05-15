"""
    Controller for the search string functionality
"""

from flask import Response


def search_string_controller(search):
    """
    Controller that handles the route logic for the search string
    :return:
    """
    if search:
        return Response({"Controller": 200})