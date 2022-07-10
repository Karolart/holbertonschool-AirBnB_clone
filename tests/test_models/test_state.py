#!/usr/bin/python3
"""
Test suits for State
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest
import os
class TestState(unittest.TestCase):
    """
    Tests for state
    """

   def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pass
    
    def test_name(self):
        """
        Test if the name atribute is right.
        """
        state_test = State()
        self.assertEqual(state_test.__class__.__name__, "State")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        state_test = State()
        self.assertEqual(state1.__class__.__name__, "State")

if __name__ == '__main__':
    unittest.main()
