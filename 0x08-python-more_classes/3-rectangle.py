#!/usr/bin/python3


class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Value height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validations errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Value width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validations errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter rectangle"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print charter #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(("#" * self.__width for i in range(self.__height)))
