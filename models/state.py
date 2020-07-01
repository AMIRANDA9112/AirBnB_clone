#!/usr/bin/python
""" create class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class state """
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
