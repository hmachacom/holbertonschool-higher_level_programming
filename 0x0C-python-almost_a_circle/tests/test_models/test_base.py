#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base





class TestBase(unittest.TestCase):
    """
    class unittest for Base
    """

    def test_id1n(self):
        """
        Check return function
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2(self):
        """
        Check return function
        """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id3(self):
        """
        Check return function
        """
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id4(self):
        """
        Check return function
        """
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id5(self):
        """
        Check return function
        """
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
