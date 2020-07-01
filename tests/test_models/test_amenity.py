#!/usr/bin/python3
"""Tests BaseModel class"""
import os
import unittest
import models
from models.user import User


class TestBase_Model(unittest.TestCase):
    """Tests for class Amenity"""

    def test_docstring(self):
        '''test if funcions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.Amenity.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Amenity.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_model is an instance of User'''
        my_model = Amenity()
        self.assertIsInstance(my_model, Amenityy)

    def test_id(self):
        '''test if the id of two instances are different'''
        my_model = Amenity()
        my_model1 = Amenity()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        my_model2 = Amenity()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = Amenity()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Amenity':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)
