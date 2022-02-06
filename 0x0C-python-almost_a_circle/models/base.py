#!/usr/bin/python3
""" Class base"""
import json


class Base:
    """Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([int]): [description]. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]
        """
        if not list_dictionaries or list_dictionaries == [None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """

        Args:
            list_objs ([type]): [description]
        """
        save = []
        for i in list_objs:
            save.append(i.to_dictionary())
        file = cls.__name__ + ".json"
        with open(file, "w") as new_file:
            new_file.write(Base.to_json_string(save))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        if not json_string or json_string == [None]:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]
        """

        new_class = cls(1, 1)
        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        """load from file"""
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as my_file:
                return [
                    (cls.create(**i)) for i in
                    Base.from_json_string(my_file.read())
                ]
        except Exception:
            return []
