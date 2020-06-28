#!/usr/bin/env python

"""
Write a class Base Model for project nBnB
"""

import uuid
from datetime import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):
        """constructor the class BaseModel"""
        
        if kwargs or kwargs != {}:
            for key in kwargs:
                self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """save the instance"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """"get atributes to dict"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['created_at'] = self.created_at.strftime(format)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['my_number'] = self.my_number
        my_dict['updated_at'] = self.updated_at.strftime(format)
        my_dict['name'] = self.name

        return my_dict

    def __str__(self):
        """print dir the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

        #angel.co/jobs
        #remoteok.io
        #weworkremotely.com