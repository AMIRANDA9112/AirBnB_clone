#!/usr/bin/env python

"""
Write a class FileStorage for project nBnB
"""

import json
from models.base_model import BaseModel


class FileStorage():
    """Store the dict data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all dict in the __objects"""
        return self.__objects

    def new(self, obj):
        """add dict in the __objects"""
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """deserealization __object in the file.json"""
        add_dict = {}

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for key, value in self.__objects.items():
                add_dict[key] = value.to_dict()
            json.dump(add_dict, f)

    def reload(self):
        """serialization the file.json"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                content_file = json.load(f)
                for k, v in content_file.items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except Exception:
            pass
