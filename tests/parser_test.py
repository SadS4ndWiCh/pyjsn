import unittest

from src.ast import KindAST
from src.lexer import Lexer
from src.parser import Parser


class ParserTest(unittest.TestCase):
    def test_parsing(self):
        source = '{"hello": "world", "foo": "bar"}'

        lexer = Lexer(source)
        parser = Parser(lexer)

        json_ast = parser.parse()
        self.assertTrue(json_ast is not None)
        self.assertEqual(json_ast.kind, KindAST.OBJECT)

        print(f"{json_ast.keys!r}")
        print(f"{json_ast.values!r}")
