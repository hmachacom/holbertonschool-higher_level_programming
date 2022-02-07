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
        b2 = Base(None)
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

    """=========================================================="""
    """Check function to_json_string """

    def test_json_String(self):
        self.assertEqual(Base.to_json_string([{"id": 55}]), '[{"id": 55}]')
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_type(self):
        r1 = Rectangle(5, 3, 1, 5, 15)
        s1 = Square(5, 1, 5, 15)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_to_json_string_Rectangle(self):
        r1 = Rectangle(5, 3, 78, 25, 15)
        list_dictionary = [r1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dictionary)) == 55)

    def test_to_json_string_Square(self):
        square = Square(18, 25, 5, 15)
        dictionary = [square.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dictionary)) == 41)

    def test_to_json_string(self):
        dictionary = {"x": 5, "width": 20, "height": 16, "y": 5, "id": 1}
        json = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue(isinstance(json, str))
        self.assertCountEqual
        (json, '[{"x": 5, "width": 20, "height": 16, "y": 5, "id": 1}]')

    def test_to_json_types(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string([], 21)

        er1 = (
            "to_json_string() missing 1 required positional argument: "
            + "'list_dictionaries'"
        )

        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(er1, str(x.exception))

        er2 = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(er2, str(x.exception))

    """=========================================================="""
    """Check function create """


if __name__ == "__main__":
    unittest.main()
