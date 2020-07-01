#!/usr/bin/python
""" create class city"""
from models.base_model import BaseModel


class city(BaseModel):
    """class city"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
