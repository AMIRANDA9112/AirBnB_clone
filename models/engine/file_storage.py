#!/usr/bin/env python3

"""
Write a class Base Model for project nBnB
"""

import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[obj.__name__ +'.'+obj.id] = obj.id

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json.loads(f.readline())
