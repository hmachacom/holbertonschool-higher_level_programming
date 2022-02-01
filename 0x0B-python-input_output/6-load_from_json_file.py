#!/usr/bin/python3
"""import module json"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a
    “JSON file”

    Args:
        filename ([json]): [file.json]
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
