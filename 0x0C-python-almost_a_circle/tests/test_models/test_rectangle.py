#!/usr/bin/python3
"""Archivo que verifica los posibles casos
de error del archivo rectangle."""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestRectangle(unittest.TestCase):
    """Todos los posibles errores"""

    r3 = Rectangle(10, 2, 0, 0, 12)

    def setUp(self):
        Base._Base__nb_objects = 0

    def testId(self):
        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(2, 3).id, 2)
        self.assertEqual(Rectangle(3, 4).id, 3)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 2, 4, 5, 15).id, 15)
        self.assertEqual(Rectangle(10, 2, 4, 5, -15).id, -15)

    def test_dimension(self):
        dim = Rectangle(2, 10)
        self.assertEqual(dim.width, 2)
        self.assertEqual(dim.height, 10)

    def test_raise_height_negative(self):
        """Check Value error in height
        """
        self.assertRaises(ValueError, Rectangle, 8, -1)

    def test_raise_width_negative(self):
        """Check Value error in width negative
        """
        self.assertRaises(ValueError, Rectangle, -2, 8)

    def test_raise_width_no_int(self):
        """Check Value error in width no int
            """
        self.assertRaises(TypeError, Rectangle, "-2", 8)

    def test_raise_height_no_int(self):
        """Check Value error in height no int
            """
        self.assertRaises(TypeError, Rectangle, 2, "straus")

    def test_raise_x_negative(self):
        """Check Value error in x
        """
        self.assertRaises(ValueError, Rectangle, 8, 2, -2)

    def test_raise_y_negative(self):
        """Check Value error in y negative
        """
        self.assertRaises(ValueError, Rectangle, 2, 8, 1, -9)

    def test_raise_y_no_int(self):
        """Check Value error in y no int
            """
        self.assertRaises(TypeError, Rectangle, 4, 8, 8, "straus")

    def test_raise_x_no_int(self):
        """Check Value error in x no int
            """
        self.assertRaises(TypeError, Rectangle, 2, 2, "straus")

    """=========================================================="""

    """Check the value id"""

    def test_id1n(self):
        """
        Check return function
        """
        r1 = Rectangle(10, 2, 0, 0, 25)
        self.assertEqual(r1.id, 25)

    def test_id2n(self):
        """
        Check return function
        """
        r2 = Rectangle(1, 1, 2, 10, 5)
        self.assertEqual(r2.id, 5)

    def test_id3n(self):
        """
        Check return function
        """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    """=========================================================="""
    """Check the value width"""

    def test_value_width(self):
        """Check the value width"""
        self.assertEqual(Rectangle(1, 2, 0, 0, 0).width, 1)
        self.assertEqual(Rectangle(3, 5, 0, 0, 0).width, 3)
        self.assertEqual(Rectangle(15, 27).width, 15)
        self.assertEqual(Rectangle(35, 15, 0, 0, 0).width, 35)
        self.assertEqual(Rectangle(78, 9, 0, 0, 0).width, 78)
        self.assertEqual(Rectangle(5, 6, 0, 0, 0).width, 5)

    """=========================================================="""
    """Check the value height"""

    def test_value_height(self):
        """Check the value height"""
        self.assertEqual(Rectangle(1, 2, 0, 0, 0).height, 2)
        self.assertEqual(Rectangle(3, 5, 0, 0, 0).height, 5)
        self.assertEqual(Rectangle(15, 27).height, 27)
        self.assertEqual(Rectangle(35, 15, 0, 0, 0).height, 15)
        self.assertEqual(Rectangle(78, 9, 0, 0, 0).height, 9)
        self.assertEqual(Rectangle(5, 6, 0, 0, 0).height, 6)

    """=========================================================="""
    """Check the value x"""

    def test_value_x(self):
        """Check the value x"""
        self.assertEqual(Rectangle(1, 2, 8, 0).x, 8)
        self.assertEqual(Rectangle(3, 5, 12, 0).x, 12)
        self.assertEqual(Rectangle(15, 27).x, 0)
        self.assertEqual(Rectangle(35, 15, 57, 0).x, 57)
        self.assertEqual(Rectangle(78, 9, 89, 0).x, 89)
        self.assertEqual(Rectangle(5, 6, 4, 0).x, 4)

    """=========================================================="""
    """Check the value x"""

    def test_value_y(self):
        """Check the value y"""
        self.assertEqual(Rectangle(1, 2, 8, 7).y, 7)
        self.assertEqual(Rectangle(3, 5, 12, 25).y, 25)
        self.assertEqual(Rectangle(15, 27).y, 0)
        self.assertEqual(Rectangle(35, 15, 57, 45).y, 45)
        self.assertEqual(Rectangle(78, 9, 89, 17).y, 17)
        self.assertEqual(Rectangle(5, 6, 4, 9).y, 9)

    """=========================================================="""
    """Check the value is instance"""

    def test_is_instance_Rectangle(self):
        """Check print"""
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r4, Rectangle)

    """=========================================================="""
    """Check the value is instance"""

    def test_is_instance_Rectangle(self):
        """Check print"""
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r4, Rectangle)

    """=========================================================="""
    """Check the methode area"""

    def test_methode_area(self):
        """Check the value area"""
        r5 = Rectangle(1, 2, 8, 7)
        self.assertEqual(r5.area(), 2)
        r5 = Rectangle(3, 5, 12, 25)
        self.assertEqual(r5.area(), 15)
        r5 = Rectangle(15, 27)
        self.assertEqual(r5.area(), 405)

    """=========================================================="""
    """Check the methode str"""

    def test_methode_str(self):
        """Check the value str"""
        r5 = Rectangle(1, 2, 8, 7, 9)
        self.assertEqual(r5.__str__(), "[Rectangle] (9) 8/7 - 1/2")

    """=========================================================="""
    """Check the methode str"""

    def test_methode_to_dictionary(self):
        """Check the value to_dictionary"""
        r5 = Rectangle(1, 2, 8, 7, 10)
        self.assertEqual(
            r5.to_dictionary(), {"width": 1, "height": 2, "x": 8, "y": 7, "id": 10}
        )

    """=========================================================="""
    """Check the methode update"""

    def test_methode_update_args(self):
        """Check the value update"""
        r5 = Rectangle(1, 2, 8, 7, 99)
        r5.update(80, 1, 1, 1, 96)
        self.assertEqual(r5.__str__(), "[Rectangle] (80) 1/96 - 1/1")

    def test_methode_update_kwargs(self):
        """Check the value update"""
        r6 = Rectangle(1, 2, 8, 7, 12)
        r6.update(width=16, x=4)
        self.assertEqual(r6.__str__(), "[Rectangle] (12) 4/7 - 16/2")

    """=========================================================="""
    """Check the methode to_json_string"""

    def test_methode_to_json_string(self):
        """Check to_json_string"""
        r5 = Rectangle(10, 7, 2, 8, 17)
        dict = r5.to_dictionary()
        self.assertEqual(
            r5.to_json_string(dict),
            '{"width": 10, "height": 7, "x": 2, "y": 8, "id": 17}',
        )
        """call the methode without parametres"""
        self.assertRaises(TypeError, r5.to_json_string)
        self.assertEqual(r5.to_json_string(("straus", "migo")), '["straus", "migo"]')


if __name__ == "__main__":
    unittest.main()
