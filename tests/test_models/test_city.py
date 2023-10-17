#!/usr/bin/python3
"""unittests for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for City class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
