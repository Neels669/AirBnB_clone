#!/usr/bin/python3
"""unittests for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for Amenity class """
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
