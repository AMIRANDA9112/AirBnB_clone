#!/usr/bin/python3
"""Unit test for base model
"""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
CurrentClass = models.base_model.BaseModel

class TestBaseClass(unittest.TestCase):
    """Tests for BasModel"""

    def testSave(self):
        """ file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def test_isinstance(self):
        """ Check if is instance """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id(self):
        """  id type """
        my_third = BaseModel()
        self.assertTrue(type(my_third.id) == str)

    def test_remove(self):
        """Executes when test finish"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict(self):
        """Test to_dict function"""
        cti1 = CurrentClass()
        cti1_dict = cti1.to_dict()
        self.assertEqual(type(cti1_dict), dict)
        self.assertIn('updated_at', cti1_dict)
        self.assertIn('created_at', cti1_dict)
        self.assertIn('__class__', cti1_dict)
        self.assertNotEqual(cti1_dict, cti1.__dict__)

if __name__ == '__main__':
    unittest.main()
