#!/usr/bin/python3
"""Class Student
"""


class Student:
    """defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
            first_name ([str])
            last_name ([str])
            age ([int])
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        """
        return self.__dict__
