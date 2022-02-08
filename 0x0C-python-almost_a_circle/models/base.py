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
        if cls.__name__ == 'Rectangle':
            new_cls = cls(1, 1)
        elif cls.__name__ == 'Square':
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
        """csv"""
        save = []
        if list_objs is not None and len(list_objs) > 0:
            save = [(i.to_dictionary()) for i in list_objs]
        with open(cls.__name__ + ".csv", "w") as my_file:
            writer = csv.writer(my_file)
            for i in save:
                for key, value in i.items():
                    writer.writerow([key, value])

    @classmethod
    def load_from_file_csv(cls):
        """Load csv"""
        if cls.__name__ == "Rectangle":
            var_ctr = 5
        elif cls.__name__ == "Square":
            var_ctr = 4
        else:
            var_ctr = 1
        try:
            with open(cls.__name__ + ".csv", mode='r') as f:
                reader = csv.reader(f)
                i = 1
                list_dir = []
                dict_from_csv = {}
                for rows in reader:
                    if i <= var_ctr:
                        dict_from_csv[rows[0]] = int(rows[1])
                        i += 1
                    else:
                        list_dir.append(dict_from_csv.copy())
                        dict_from_csv[rows[0]] = int(rows[1])
                        i = 1
                list_dir.append(dict_from_csv.copy())
                return [cls.create(**i) for i in list_dir]
        except Exception:
            return []
