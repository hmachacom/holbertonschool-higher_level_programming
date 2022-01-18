#!/usr/bin/python3
""" class square new """


class Square:
    """class square empty"""

    pass

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        """ Validations errors """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return area of the square"""
        return self.__size * self.__size
