#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init self"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = "#"

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print charter #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for i in range(self.__height)
        )

    def __repr__(self):
        """ Print instans for developmen"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(width=size, height=size)

