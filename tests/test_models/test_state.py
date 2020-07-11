#!/usr/bin/python3
"""Unit test for State Class
"""

import unittest
from models.state import State
from models.base_model import BaseModel
import os


class TestCityClass(unittest.TestCase):
    """Tests City class"""

    def setUp(self):
        """init for  each test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docs(self):
        """ check documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test inheritance of BaseModel """
        my_user = State()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test type of attributes """
        my_user = State()
        self.assertTrue(type(my_user.name) == str)


if __name__ == '__main__':
    unittest.main()
