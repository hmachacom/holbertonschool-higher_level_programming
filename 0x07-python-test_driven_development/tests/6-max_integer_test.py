#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class unittest for max_integer
    """

    def test_return(self):
        """
        Check return function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_difference(self):
        """
        Check difference value
        """
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 1)

    def test_empty(self):
        """
        Check list is empty
        """
        result = max_integer()
        self.assertIsNone(result)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer(([1, "s", 3, 4]), 4)

    def test_string_Equal(self):
        """
        Check result is 0
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_check_tuple(self):
        """
        Check value tuple
        """
        self.assertEqual(max_integer((5, 10)), 10)

    def test_float(self):
        """
        Check result float
        """
        self.assertEqual(max_integer([1, 8.1, 7]), 8.1)

    def test_argument(self):
        """Check argument is a list"""
        with self.assertRaises(TypeError):
            max_integer(15)

    def test_argument_sum(self):
        """Check sum Arguments"""
        self.assertEqual(max_integer([10 + 10, 20]), 20)


if __name__ == "__main__":
    unittest.main()
