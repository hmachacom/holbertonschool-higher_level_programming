#!/usr/bin/python3
""" class square new """


class Square:
    """class square empty"""

    pass

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ value size"""
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

    @property
    def position(self):
        """ value position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Validations errors """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print a square"""
        areas = self.__size
        if areas > 0:
            for s in range(0, self.position[1]):
                print()
            for i in range(areas):
                for m in range(self.position[0]):
                    print(" ", end="")
                for j in range(areas):
                    print("#", end="")
                print()
        else:
            print()
