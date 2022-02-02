#!/usr/bin/python3
"""Module that holds class Student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key_1 in attrs:
            if key_1 in self.__dict__.keys():
                my_dict[key_1] = self.__dict__[key_1]
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        new_dict = self.__dict__
        for attr in json.keys():
            for new_d1 in new_dict.keys():
                if attr == new_d1:
                    new_dict[new_d1] = json[attr]
        return new_dict
