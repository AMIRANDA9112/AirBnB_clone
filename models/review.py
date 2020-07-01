#!/usr/bin/python
""" create class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
