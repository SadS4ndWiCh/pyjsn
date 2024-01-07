import unittest

from src.tokens import Tokens
from src.lexer import Lexer

class LexerTesting(unittest.TestCase):
    def test_tokenization(self):
        json = '{"foo":"bar", "num": 12, "bool": false, "obj": { "inner": "obj" }}'

        tokens = [
                (Tokens.OPBRACE, "{"),
                (Tokens.STRING, "foo"),
                (Tokens.COLON, ":"),
                (Tokens.STRING, "bar"),
                (Tokens.COMMA, ","),
                (Tokens.STRING, "num"),
                (Tokens.COLON, ":"),
                (Tokens.NUMBER, "12"),
                (Tokens.COMMA, ","),
                (Tokens.STRING, "bool"),
                (Tokens.COLON, ":"),
                (Tokens.FALSE, "false"),
                (Tokens.COMMA, ","),
                (Tokens.STRING, "obj"),
                (Tokens.COLON, ":"),
                (Tokens.OPBRACE, "{"),
                (Tokens.STRING, "inner"),
                (Tokens.COLON, ":"),
                (Tokens.STRING, "obj"),
                (Tokens.CLBRACE, "}"),
                (Tokens.CLBRACE, "}"),
                (Tokens.EOF, "")
        ]

        lex = Lexer(json)

        for expectedType, expectedLiteral in tokens:
            tok = lex.nextToken()

            self.assertEqual(expectedType, tok.type)
            self.assertEqual(expectedLiteral, tok.literal)

