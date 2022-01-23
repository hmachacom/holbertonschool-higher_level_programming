#!/usr/bin/python3
"""
This function print a string token specified
"""


def text_indentation(text):
    """
    This function print a string token specified
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_aux = text.replace(". ", ".\n\n")
    text_aux = text_aux.replace("? ", "?\n\n")
    text_aux = text_aux.replace(": ", ":\n\n")
    print(text_aux)
