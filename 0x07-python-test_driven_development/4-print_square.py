#!/usr/bin/python3
"""
This function print a square specified
"""


def print_square(size):
    """
    This function print a square specified
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
