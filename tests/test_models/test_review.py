#!/usr/bin/python3
"""Unit test for review Class
"""

import unittest
from models.review import Review
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
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test inheritance of BaseModel """
        my_user = Review()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test type of attributes """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) == str)
        self.assertTrue(type(my_Review.user_id) == str)
        self.assertTrue(type(my_Review.text) == str)

if __name__ == '__main__':
    unittest.main()
