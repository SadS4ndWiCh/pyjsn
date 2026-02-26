import unittest

from src.ast import KindAST, ArrayAST, ObjectAST
from src.lexer import Lexer
from src.parser import Parser


class ParserTest(unittest.TestCase):
    def test_parsing_object(self):
        source = '{"hello": "world", "foo": "bar", "num": 12, "floats": 53.22, "truesh": true, "falsesh": false}'

        keys = ["hello", "foo", "num", "floats", "truesh", "falsesh"]
        values = ["world", "bar", 12.0, 53.22, True, False]

        lexer = Lexer(source)
        parser = Parser(lexer)

        json_ast = parser.parse()
        self.assertTrue(json_ast is not None)
        self.assertEqual(json_ast.kind, KindAST.OBJECT)
        self.assertCountEqual(json_ast.keys, keys)
        self.assertCountEqual(json_ast.values, values)

        for i, (key, val) in enumerate(zip(keys, values)):
            self.assertEqual(json_ast.keys[i], key)
            self.assertEqual(json_ast.values[i], val)

    def test_parsing_array(self):
        source = '["world", 12, false, {"foo": "bar"}]'

        lexer = Lexer(source)
        parser = Parser(lexer)

        json_ast = parser.parse()
        self.assertTrue(json_ast is not None)
        self.assertEqual(json_ast.kind, KindAST.ARRAY)
        self.assertEqual(len(json_ast.items), 4)
        self.assertEqual(json_ast.items[3].kind, KindAST.OBJECT)
