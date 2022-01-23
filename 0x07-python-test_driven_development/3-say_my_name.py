#!/usr/bin/python3
"""
This function print a string specified
"""


def say_my_name(first_name, last_name=""):
    """
    This function print a string specified
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
