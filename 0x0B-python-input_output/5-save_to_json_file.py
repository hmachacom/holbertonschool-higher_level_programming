#!/usr/bin/python3
""" import module json"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj ([JSON])
        filename ([FILE])
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
