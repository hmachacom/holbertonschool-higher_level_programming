#!/usr/bin/python3
"""[function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON
    representation of an object (string)

    Args:
        my_obj ([string])
    """
    return json.dumps(my_obj)
