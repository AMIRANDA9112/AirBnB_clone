#!/usr/bin/python3
'''Tests FileStorage class'''
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFile_Storage(unittest.TestCase):
    '''tests Storage'''

    def test_1(self):
        """  Test Dictionary """
        model = BaseModel()
        model.save()
        new_object = models.storage.all()
        self.assertEqual(dict, type(new_object))

    def test_2(self):
        """check if my_model is an instance of BaseModel"""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)
    
    def test_3(self):
        """test docstring"""
        msj = "Module doesnt have docstring"
        obj = models.engine.file_storage.__doc__
        self.assertIsNotNone(obj, msj)  # Modules
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj)  # Classes
    
    def test_4(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)