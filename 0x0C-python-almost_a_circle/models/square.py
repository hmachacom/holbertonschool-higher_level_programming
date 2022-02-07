#!/usr/bin/python3
"""import Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([int])
            x (int, optional): Defaults to 0.
            y (int, optional):Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Value size

        Args:
            size ([int])
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Print
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size)

    def update(self, *args, **kwargs):
        """[summary]
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """to_dictionary
        """
        return {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
