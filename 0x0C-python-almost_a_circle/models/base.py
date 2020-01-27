#!/usr/bin/python3
"""Base class"""

import json
import csv


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init the base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string in dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON"""
        if len(json_string) == 0 or json_string is None:
            return ([])
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(filename, 'w') as fle:
            fle.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """Create a instance"""
        if cls.__name__ is "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ is "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Loads a instance"""
        filename = cls.__name__ + ".json"
        new_list = []
        with open(filename, 'r') as f:
            new_list = cls.from_json_string(f.read())
        for i, j in enumerate(new_list):
            new_list[i] = cls.create(**new_list[i])
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_f:
            save = csv.writer(csv_f)
            if cls.__name__ is "Square":
                for i in list_objs:
                    save.writerow([i.id, i.size, i.x, i.y])
            elif cls.__name__ is "Rectangle":
                for i in list_objs:
                    save.writerow([i.id, i.width, i.height, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes"""
        filename = cls.__name__ + ".csv"
        loads = []
        with open(filename, 'r') as csv_f:
            read = csv.reader(csv_f)
            for i in read:
                if cls.__name__ is "Square":
                    load = {"id": int(i[0]), "size": int(i[1]),
                            "x": int(i[2]), "y": int(i[3])}
                elif cls.__name__ is "Rectangle":
                    load = {"id": int(i[0]), "width": int(i[1]),
                            "height": int(i[2]), "x": int(i[3]),
                            "y": int(i[4])}
                loads.append(cls.create(**load))
        return loads
