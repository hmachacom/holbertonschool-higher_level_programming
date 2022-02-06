#!/usr/bin/python3
from models.base import Base

"""Class Rectangle"""


class Rectangle(Base):
    """Class Rectangle

    Args:
        Base ([type]): [description]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init value

        Args:
            width ([int])
            height ([int])
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([int], optional):  Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """[summary]
            """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    @property
    def width(self):
        """value width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Value width

        Args:
            width ([int])
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """value height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Value height

        Args:
            height ([int])
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """value x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Value x

        Args:
            x ([int])
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """value y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Value y

        Args:
            y ([int])
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Value area"""
        return self.__width * self.__height

    def display(self):
        """ Print rectangle"""
        if self.__x > 1:
            for x in range(self.__x):
                print("")
        for i in range(self.__height):
            print(" " * self.__y + "#" * self.__width)

    def __str__(self):
        """Print """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            str(self.id),
            str(self.__x),
            str(self.__y),
            str(self.__width),
            str(self.__height),
        )

    def to_dictionary(self):
        """to_dictionary
        """
        return {
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
            "id": self.id,
        }
