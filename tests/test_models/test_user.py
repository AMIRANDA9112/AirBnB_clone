#!/usr/bin/python3
"""Unit test for the file storage class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import os


class TestUserClass(unittest.TestCase):
    """Tests for User"""

    def setUp(self):
        """init for each test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docs(self):
        """ check documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test inheritance of BaseModel """
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test type of attributes """
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)


if __name__ == '__main__':
    unittest.main()
