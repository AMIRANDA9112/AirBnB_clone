#!/usr/bin/python3
"""Unit test for amenity Class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os

class TestAmenityClass(unittest.TestCase):
    """Tests Amenity class"""

    def setUp(self):
        """init for  each test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docs(self):
        """ check documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test inheritance of BaseModel """
        my_user = Amenity()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test type of attributes """
        my_user = Amenity()
        self.assertTrue(type(my_user.name) == str)


if __name__ == '__main__':
    unittest.main()