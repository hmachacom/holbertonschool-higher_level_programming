#!/usr/bin/python3
"""Archivo que verifica los posibles casos
de error del archivo square."""
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import unittest


class testSquare(unittest.TestCase):
    """Todas las funciones posibles"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_raise_height_negative(self):
        self.assertRaises(ValueError, Square, 8, -1)

    def test_raise_width_negative(self):
        self.assertRaises(ValueError, Square, -2, 8)

    def test_raise_width_no_int(self):
        self.assertRaises(TypeError, Square, "-9", 8)

    def test_raise_height_no_int(self):
        self.assertRaises(TypeError, Square, 2, "misterios")

    def test_raise_x_negative(self):
        self.assertRaises(ValueError, Square, 8, 2, -2)

    def test_raise_y_negative(self):
        self.assertRaises(ValueError, Square, 2, 8, -1)

    def test_raise_y_no_int(self):
        self.assertRaises(TypeError, Square, 4, 8, "misterios")

    def test_raise_x_no_int(self):
        self.assertRaises(TypeError, Square, 2, 2, "misterios")

    def test_sinexepcion(self):
        """Test Square class: check for missing args."""
        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(x.exception),
        )

    """=========================================================="""

    def test_id1n(self):
        """
        Check return function
        """
        r1 = Square(10, 2, 0, 25)
        self.assertEqual(r1.id, 25)

    def test_id2n(self):
        """
        Check return function
        """
        r2 = Square(2, 10, 5, 45)
        self.assertEqual(r2.id, 45)

    def test_id3n(self):
        """
        Check return function
        """
        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.id, 12)

    """=========================================================="""
    """Check the value width"""

    def test_value_width(self):
        """Check the value width"""
        self.assertEqual(Square(1, 2, 0, 0).width, 1)
        self.assertEqual(Square(3, 5, 0, 0).width, 3)
        self.assertEqual(Square(15, 27).width, 15)
        self.assertEqual(Square(35, 15, 0, 0).width, 35)
        self.assertEqual(Square(78, 9, 0, 0).width, 78)
        self.assertEqual(Square(5, 6, 0, 0).width, 5)

    """=========================================================="""
    """Check the value height"""

    def test_value_height(self):
        """Check the value height"""
        self.assertEqual(Square(1, 2, 0, 0).height, 1)
        self.assertEqual(Square(3, 5, 0, 0).height, 3)
        self.assertEqual(Square(15, 27).height, 15)
        self.assertEqual(Square(35, 15, 0, 0).height, 35)
        self.assertEqual(Square(78, 9, 0, 0).height, 78)
        self.assertEqual(Square(5, 6, 0, 0).height, 5)

    """=========================================================="""
    """Check the value x"""

    def test_value_x(self):
        """Check the value x"""
        self.assertEqual(Square(1, 2, 8, 0).x, 2)
        self.assertEqual(Square(3, 5, 12, 0).x, 5)
        self.assertEqual(Square(15, 27).x, 27)
        self.assertEqual(Square(35, 15, 57, 0).x, 15)
        self.assertEqual(Square(78, 9, 89, 0).x, 9)
        self.assertEqual(Square(5, 6, 4, 0).x, 6)

    """=========================================================="""
    """Check the value x"""

    def test_value_y(self):
        """Check the value y"""
        self.assertEqual(Square(1, 2, 8, 7).y, 8)
        self.assertEqual(Square(3, 5, 12, 25).y, 12)
        self.assertEqual(Square(15, 27).y, 0)
        self.assertEqual(Square(35, 15, 57, 45).y, 57)
        self.assertEqual(Square(78, 9, 89, 17).y, 89)
        self.assertEqual(Square(5, 6, 4, 9).y, 4)

    def test_atribute_size(self):
        """Test Square class: check for size attribute."""
        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 2)
        self.assertEqual(s2.size, 9)

    """=========================================================="""
    """Check the value is instance"""

    def test_is_instance_Square(self):
        """Check print"""
        r4 = Square(10, 2, 0, 12)
        self.assertIsInstance(r4, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(r4, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    """=========================================================="""
    """Check the methode area"""

    def test_methode_area(self):
        """Check the value area"""
        r5 = Square(1, 2, 8, 7)
        self.assertEqual(r5.area(), 1)
        r5 = Square(3, 5, 12, 25)
        self.assertEqual(r5.area(), 9)
        r5 = Square(15, 27)
        self.assertEqual(r5.area(), 225)

    """=========================================================="""
    """Check the methode str"""

    def test_methode_str(self):
        """Check the value str"""
        r5 = Square(1, 2, 8, 7)
        self.assertEqual(r5.__str__(), "[Square] (7) 2/8 - 1")

    """=========================================================="""
    """Check the methode dictionary"""

    def test_methode_to_dictionary(self):
        """Check the value to_dictionary"""
        r5 = Square(1, 2, 8, 7)
        self.assertEqual(r5.to_dictionary(), {"size": 1, "x": 2, "y": 8, "id": 7})

    """=========================================================="""
    """Check the methode update"""

    def test_methode_update_args(self):
        """Check the value update"""
        r5 = Square(1, 2, 8, 7)
        r5.update(16, 25)
        self.assertEqual(r5.__str__(), "[Square] (16) 2/8 - 25")

    def test_methode_update_kwargs(self):
        """Check the value update"""
        r5 = Square(1, 2, 8, 7)
        r5.update(size=16, x=4)
        self.assertEqual(r5.__str__(), "[Square] (7) 4/8 - 16")

    def test_update_error(self):
        """Test for update method on Square with wrong types."""
        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))

    """=========================================================="""
    """Check the methode to_json_string"""

    def test_methode_to_json_string(self):
        """Check to_json_string"""
        r5 = Square(10, 7, 2, 17)
        dict = r5.to_dictionary()
        self.assertEqual(
            r5.to_json_string(dict), '{"size": 10, "x": 7, "y": 2, "id": 17}'
        )
        """call the methode without parametres"""
        self.assertRaises(TypeError, r5.to_json_string)
        self.assertEqual(
            r5.to_json_string(("misterios", "spirit")), '["misterios", "spirit"]'
        )
