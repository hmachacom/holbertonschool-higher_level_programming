#!/usr/bin/python3
""" ::::::::::::::::"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """:::::::::::"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def __str__(self):
        """_:::::::::::::::::::"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """::::::::::::"""
        return self.__width * self.__height
