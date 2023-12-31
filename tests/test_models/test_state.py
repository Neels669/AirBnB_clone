#!/usr/bin/python3
"""unittests for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for State class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
