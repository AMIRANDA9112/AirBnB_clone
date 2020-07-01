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
        '''check if my_model is an instance of BaseModel'''
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)