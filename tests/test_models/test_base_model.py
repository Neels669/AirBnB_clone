#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for class"""

    def test_constructor(self):
        """Test if attributes are created"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_save_method(self):
        """Check updated_at func"""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Check to_dict func"""
        my_model = BaseModel()
        my_model.name = "Neelam"
        my_model.my_number = 89
        model_dict = my_model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)


if __name__ == '__main__':
    unittest.main()
