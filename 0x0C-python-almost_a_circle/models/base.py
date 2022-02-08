#!/usr/bin/python3
""" Class base"""
import json
import csv


class Base:
    """Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """attribute initialization

        Args:
            id ([int]): . Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string
        representation of ``list_dictionaries``

        Args:
            list_dictionaries ([list])
        """
        if not list_dictionaries or list_dictionaries == [None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        returns the JSON
        string representation of ``list_dictionaries``
        Args:
            list_objs ([list])
        """
        save = []
        if list_objs is not None and len(list_objs) > 0:
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
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an
        instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_cls = cls(1, 1)
        elif cls.__name__ == "Square":
            new_cls = cls(1)
        new_cls.update(**dictionary)
        return new_cls

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as my_file:
                return [
                    (cls.create(**i)) for i in
                    Base.from_json_string(my_file.read())
                ]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """create file .csv"""
        line = []
        with open(cls.__name__ + ".csv", "w") as my_file:
            if list_objs is None or len(list_objs) <= 0:
                my_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    line = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    line = ["id", "size", "x", "y"]
            var = csv.DictWriter(my_file, fieldnames=line)
            for iter in list_objs:
                var.writerow(iter.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """read the function"""
        try:
            with open(cls.__name__ + ".csv", "r") as my_file:
                if cls.__name__ == "Rectangle":
                    line = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    line = ["id", "size", "x", "y"]
                read_file = csv.DictReader(my_file, fieldnames=line)
                dict_ni = [
                    dict([clave, int(valor)] for clave, valor in iter.items())
                    for iter in read_file
                ]
                return [cls.create(**dict_l) for dict_l in dict_ni]
        except Exception:
            return []
