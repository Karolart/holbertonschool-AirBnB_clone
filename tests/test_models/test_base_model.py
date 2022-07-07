#!/usr/bin/python3
"""
Test suits for the base model
"""

import os
import re
import json
import uuid
import unittest
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """
    @classmethod
    def setUpClass(cls):
        """
        Classes needed for testing
        """
        pass

    def test_instance(self):
        """
        Tests basic imputs for the BaseModel class
        """
        my_model = BaseModel()
         self.assertIsInstance(my_model, BaseModel)

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass
    
if __name__ == '__main__':
    unittest.main()
