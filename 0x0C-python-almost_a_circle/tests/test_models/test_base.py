#!/usr/bin/python3
"""test"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import os


class BaseTest(unittest.TestCase):
    """test class Base"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Id(self):
        base0 = Base()
        self.assertEqual(base0.id, 1)

    def test_Id_Non(self):
        base1 = Base(None)
        self.assertEqual(base1.id, 1)

    def test_Id_posi(self):
        base2 = Base(15)
        self.assertEqual(base2.id, 15)

    def test_ID_negative(self):
        base3 = Base(-15)
        self.assertEqual(base3.id, -15)

    def test_ID_float(self):
        base4 = Base(1.1)
        self.assertEqual(base4.id, 1.1)

    def test_combinacion(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(15).id, 15)
        self.assertEqual(Base(None).id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(-15).id, -15)

    def test_Type_Instance(self):
        typ = Base()
        self.assertEqual(type(typ), Base)
        self.assertTrue(isinstance(typ, Base))

    def test_json_String(self):
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_type(self):
        rec = Rectangle(5, 3, 1, 5, 15)
        cua = Square(5, 1, 5, 15)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([cua.to_dictionary()])))

    def test_to_json_string_Rec(self):
        rec = Rectangle(5, 3, 1, 5, 15)
        dict = [rec.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict)) == 53)

    def test_to_json_string_Squ(self):
        square = Square(5, 1, 5, 15)
        dict = [square.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict)) == 39)

    def test_to_json_string(self):
        new_dict = {"x": 5, "width": 20, "height": 16, "y": 5, "id": 1}
        json = Base.to_json_string([new_dict])
        self.assertTrue(isinstance(new_dict, dict))
        self.assertTrue(isinstance(json, str))
        self.assertCountEqual
        (json, '[{"x": 5, "width": 20, "height": 16, "y": 5, "id": 1}]')

    def test_to_json_string_none(self):
        json = Base.to_json_string([])
        self.assertEqual(json, "[]")
        json2 = Base.to_json_string(None)
        self.assertEqual(json2, "[]")

    def test_to_json_string_2Dic(self):
        cua = Square(5, 1, 5, 15)
        rec = Rectangle(5, 3, 1, 5, 15)
        dict = [cua.to_dictionary(), rec.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict)) == 92)

    def test_to_json_types(self):
        """test for to json string"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string([], 21)

        s1 = (
            "to_json_string() missing 1 required "
            + "positional argument: "
            + "'list_dictionaries'"
        )

        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))

        s2 = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def test_save_to_file_rectangle(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        rec2.id = 2
        rec1.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as myfile:
            x = json.loads(myfile.read())

        diccionarios = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0},
        ]

        self.assertEqual(x, diccionarios)

    def test_save_to_file_square(self):
        cua1 = Square(1, 2, 3, 4)
        cua2 = Square(5)
        cua2.id = 6
        cua2.save_to_file([cua1, cua2])
        with open("Square.json", "r") as file:
            x = json.loads(file.read())

        diccionarios = [
            {"y": 3, "x": 2, "id": 4, "size": 1},
            {"y": 0, "x": 0, "id": 6, "size": 5},
        ]

        self.assertEqual(x, diccionarios)

    def test_save_to_file_RectNone(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec1.save_to_file(None)
        with open("Rectangle.json", "r") as myfile:
            x = json.loads(myfile.read())
        diccionarios = []
        self.assertEqual(x, diccionarios)

    def test_save_to_file_SqutNone(self):
        cua1 = Square(1, 2, 3, 4)
        cua1.save_to_file(None)
        with open("Square.json", "r") as myfile:
            x = json.loads(myfile.read())
        diccionarios = []
        self.assertEqual(x, diccionarios)

    def test_save_to_file_noArgv(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_MasArgv(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 1)

    def test_save_to_file_empate(self):
        Square.save_to_file([])
        with open("Square.json", "r") as myfile:
            self.assertEqual("[]", myfile.read())

    def test_from_json_strings(self):
        dic = '{"primero": 1, "segundo": 2}'
        diccio = json.loads(dic)
        base = Base(10)
        self.assertEqual(base.from_json_string(dic), diccio)
        self.assertEqual(base.from_json_string(None), [])
        self.assertEqual(base.from_json_string("[]"), [])

    def test_from_json_string_normal(self):

        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string([8, 9])
            self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string({1: "Hola", 2: "Holi"})
            self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string(1.1)
            self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError):
            Base.from_json_string()

        with self.assertRaises(TypeError):
            Base.from_json_string([], 2)

    def test_from_json_strings_type(self):
        dic = [{"id": 1, "width": 2, "height": 6}]
        json_list = Rectangle.to_json_string(dic)
        json_o = Rectangle.from_json_string(json_list)
        self.assertEqual(list, type(json_o))

    def test_from_json_strings_Rect(self):
        dic = [{"id": 1, "width": 2, "height": 6}]
        json_list = Rectangle.to_json_string(dic)
        json_o = Rectangle.from_json_string(json_list)
        self.assertEqual(dic, json_o)

    def test_from_json_strings_Cuad(self):
        dic = [{"id": 1, "size": 7}]
        json_list = Square.to_json_string(dic)
        json_o = Square.from_json_string(json_list)
        self.assertEqual(dic, json_o)

    def test_from_json_strings_Cuad_Mul(self):
        dic = [{"id": 1, "size": 7}, {"id": 2, "size": 8}]
        json_list = Square.to_json_string(dic)
        json_o = Square.from_json_string(json_list)
        self.assertEqual(dic, json_o)

    def test_from_json_strings_Rect_Mul(self):
        dic = [{"id": 1, "width": 2, "height": 6}, {"id": 2, "width": 3, "height": 7}]
        json_list = Rectangle.to_json_string(dic)
        json_o = Rectangle.from_json_string(json_list)
        self.assertEqual(dic, json_o)

    def test_from_json_strine_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_strine_empate(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_create(self):
        dicci = {"y": 5, "x": 4, "id": 1, "width": 2, "height": 3}
        instancia = Rectangle.create(**dicci)
        self.assertEqual(type(instancia), Rectangle)
        self.assertEqual(instancia.__str__(), "[Rectangle] (1) 4/5 - 2/3")

        dicci = {"y": 5, "x": 4, "id": 1, "size": 2}
        instancia = Square.create(**dicci)
        self.assertEqual(type(instancia), Square)
        self.assertEqual(instancia.__str__(), "[Square] (1) 4/5 - 2")

    def test_create_normal(self):
        rec = Rectangle(3, 5, 1)
        rec_Dic = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_Dic)
        self.assertEqual(str(rec), str(rec2))
        self.assertFalse(rec is rec2)
        self.assertFalse(rec == rec2)

        squ = Square(3, 5)
        squ_Dic = squ.to_dictionary()
        squ2 = Square.create(**squ_Dic)
        self.assertEqual(str(squ), str(squ2))
        self.assertFalse(squ is squ2)
        self.assertFalse(squ == squ2)

    def test_create_error(self):
        with self.assertRaises(TypeError) as error:
            rec = "Dolor"
            rec2 = Rectangle.create(rec)
            self.assertEqual(
                "create() takes 1 positional argument but 2 were given",
                str(error.exception),
            )

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        lista = Rectangle.load_from_file()
        self.assertEqual(type(lista), list)
        self.assertEqual(len(lista), 0)

    def test_load_from_file_dic(self):
        lista = [
            {"y": 4, "x": 3, "id": 5, "width": 1, "height": 2},
            {"y": 0, "x": 0, "id": 8, "width": 6, "height": 7},
        ]
        with open("Rectangle.json", "w") as myfile:
            myfile.write(Rectangle.to_json_string(lista))
        instancias = Rectangle.load_from_file()
        self.assertEqual(type(instancias), list)
        self.assertEqual(len(instancias), 2)
        self.assertEqual(instancias[0].__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(instancias[1].__str__(), "[Rectangle] (8) 0/0 - 6/7")

    def test_load_from_file_Cua(self):
        try:
            os.remove("Square.json")
        except Exception:
            pass
        lista = Square.load_from_file()
        self.assertEqual(type(lista), list)
        self.assertEqual(len(lista), 0)

    def test_load_from_file_dic_Cua(self):
        lista = [
            {"y": 3, "x": 2, "id": 4, "size": 1},
            {"y": 0, "x": 0, "id": 6, "size": 5},
        ]
        with open("Square.json", "w") as myfile:
            myfile.write(Square.to_json_string(lista))
        instancias = Square.load_from_file()
        self.assertEqual(type(instancias), list)
        self.assertEqual(len(instancias), 2)
        self.assertEqual(instancias[0].__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(instancias[1].__str__(), "[Square] (6) 0/0 - 5")

    def test_load_from_file_reads_file(self):
        r1 = Square(4, 5, 9, 30)
        r2 = Square(7, 3, 8, 30)
        list_r_input = [r1, r2]
        Square.save_to_file(list_r_input)
        list_r_output = Square.load_from_file()

        self.assertIsInstance(list_r_output, list)
        self.assertFalse(len(list_r_output) == 0)

    def test_load_from_file_empty_file(self):
        list_instances = Square.load_from_file()

        self.assertIsInstance(list_instances, list)
        self.assertFalse(len(list_instances) == 0)

    def test_load_from_file_None(self):
        lista = Rectangle.load_from_file()
        self.assertEqual(lista, [])

    def test_load_from_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(2)

    def __name__(self):
        unittest.main()
