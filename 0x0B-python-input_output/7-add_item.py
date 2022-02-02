#!/usr/bin/python3
"""import modulo"""
import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
read_file = __import__("0-read_file").read_file

filename = "add_item.json"
li = []

try:
    li = load_from_json_file(filename)
except Exception:
    li = []
for i in sys.argv[1:]:
    li.append(i)
save_to_json_file(li, filename)
