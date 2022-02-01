#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters
"""


def write_file(filename="", text=""):
    """Read text in a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
