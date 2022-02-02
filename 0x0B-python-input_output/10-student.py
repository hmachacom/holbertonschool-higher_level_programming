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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        """
        if attrs is None:
            return self.__dict__
        my_dic = {}
        for key_1 in attrs:
            if key_1 in self.__dict__.keys():
                my_dic[key_1] = self.__dict__[key_1]
        return my_dic
