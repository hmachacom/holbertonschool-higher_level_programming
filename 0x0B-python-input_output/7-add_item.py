#!/usr/bin/python3
"""import modulo"""
import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
read_file = __import__("0-read_file").read_file

filename = "add_item.json"
li = []

with open(filename, mode="a", encoding="utf-8"):
    with open(filename, mode="r", encoding="utf-8") as f:
        if len(f.read()) != 0:
            li = load_from_json_file(filename)
            for i in sys.argv[1:]:
                li.append(i)
            save_to_json_file(li, filename)
        else:
            save_to_json_file(li, filename)
