#!/usr/bin/python3
import unittest
from models.base import Base
"""  Creating test cases for the base module """


class test_base(unittest.TestCase):
    """ testing case """
    def test_id_none(self):
        """ test when id is None """
        t = Base()
        self.assertEqual(1, t.id)

    def test_id(self):
        """ when id is not None """
        t = Base(7)
        self.assertEqual(7, t.id)

    def test_id_negative(self):
        """when id is -ve"""
        t = Base(-12)
        self.assertEqual(-12, t.id)
