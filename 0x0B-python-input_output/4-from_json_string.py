#!/usr/bin/python3
""" import module json"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str ([JSON])
    """
    return json.loads(my_str)
