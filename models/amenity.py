#!/usr/bin/python
""" create class amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
