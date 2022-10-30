#!/usr/bin/python3
from models.base import Base
from models.rectangle import
""" Test cases for Rectangle Module"""


class test_rectangle(unittest.TestCase):
    """ Testing Rectangle"""
    def setUp(self):
        """init instance with witdh and height"""
        self.rec = rectangle(6, 10)

    def tearDown(self):
        """Deleting created instance"""
        del self.rec

    def test_witdh(self):
        """testing width getter"""
        self.assertEqual(6, self.rec.width)

    def test_height(self):
        """test height getter"""
        self.assertEqual(10, self.rec.height)

    def test_x(self):
        """tests x getter and setter"""
        self.rec.x = 21
        self.assertEqual(21, self.rec.x)

    def test_y(self):
        """ Tests y's getter and setter."""
        self.rec.y = 12
        self.assertEqual(12, self.rec.y)

    def test_rectangle_id(self):
        """ Tests rectangle's id"""
        r = Rectangle(12, 21, 0, 0, 14)
        self.assertEqual(14, r.id)

    def test_width_str(self):
        """ Tests what happens when width is string"""
        with self.assertRaises(TypeError):
            r = Rectangle("2", 12)

    def test_width_bool(self):
        """ Tests what happens when width is Boolean"""
        with self.assertRaises(TypeError):
            r = Rectangle(True, 12)

    def test_height_str(self):
        """ Tests what happens when height is string"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, "12")

    def test_height_bool(self):
        """ Tests what happens when height is Boolean"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, False)

    def test_x_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, "46")

    def test_x_bool(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, True)

    def test_y_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_y_bool(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, True)

    def test_width_negative(self):
        """ Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

    def test_height_zero(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 0)
