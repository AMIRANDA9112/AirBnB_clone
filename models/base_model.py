#!/usr/bin/python3

"""
Write a class Base Model for project nBnB
"""

import uuid
from datetime import datetime
import models


class BaseModel():

    def __init__(self, *args, **kwargs):
        """constructor the class BaseModel"""

        if kwargs or kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save the instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"get atributes to dict"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = {}
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.strftime(format)
        my_dict['updated_at'] = self.updated_at.strftime(format)

        return my_dict

    def __str__(self):
        """print dir the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
