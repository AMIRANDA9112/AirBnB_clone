#!/usr/bin/python3
"""Unit test for storage class
"""
import unittest

from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """"tests Storage"""


    def setUp(self):
        """init for each test"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_instance(self):
        """ Check inheritance """
        self.assertIsInstance(storage, FileStorage)

    def test_doc(self):
        """ tests for documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_dict(self):
        """ Test """
        my_obj = FileStorage()
        my_dict = my_obj.all()
        self.assertTrue(type(my_dict) == dict)


if __name__ == '__main__':
    unittest.main()
