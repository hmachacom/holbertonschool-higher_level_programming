#!/usr/bin/python3
""" ........................"""


class BaseGeometry:
    """Write an empty class BaseGeometry"""

    def area(self):
        """is empty"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """::::::::::"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
