#!/usr/bin/python3
""" ::::::::::::::::"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """":::::::::::::::"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """_:::::::::::::::::::"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
