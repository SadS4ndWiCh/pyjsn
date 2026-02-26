import unittest

from src.lexer import Kind, Lexer


class LexerTesting(unittest.TestCase):
    def test_read_chars(self):
        source = "{}"

        lexer = Lexer(source)
        self.assertEqual(lexer.read_char(), "{")
        self.assertEqual(lexer.read_char(), "}")

    def test_eat_space(self):
        source = "    }      {"

        lexer = Lexer(source)
        lexer.eat_space()
        self.assertEqual(lexer.read_char(), "}")

        lexer.eat_space()
        self.assertEqual(lexer.read_char(), "{")

    def test_read_number(self):
        source = "12.25."

        lexer = Lexer(source)
        token = lexer.next_token()

        self.assertEqual(token.kind, Kind.NUMBER)
        self.assertEqual(token.literal, "12.25")

        token = lexer.next_token()
        self.assertEqual(token.kind, Kind.UNKNOWN)
        self.assertEqual(token.literal, ".")

    def test_read_ident(self):
        source = "true false"

        lexer = Lexer(source)

        token = lexer.next_token()
        self.assertEqual(token.kind, Kind.TRUE)
        self.assertEqual(token.literal, "true")

        token = lexer.next_token()
        self.assertEqual(token.kind, Kind.FALSE)
        self.assertEqual(token.literal, "false")

    def test_next_token(self):
        tokens = [
            (Kind.OP_BRACE, "{"),
            (Kind.STRING, "hello"),
            (Kind.COLON, ":"),
            (Kind.STRING, "world"),
            (Kind.COMMA, ","),
            (Kind.STRING, "foo"),
            (Kind.COLON, ":"),
            (Kind.OP_BRACKET, "["),
            (Kind.STRING, "bar"),
            (Kind.COMMA, ","),
            (Kind.NUMBER, "12.53"),
            (Kind.COMMA, ","),
            (Kind.TRUE, "true"),
            (Kind.COMMA, ","),
            (Kind.FALSE, "false"),
            (Kind.COMMA, ","),
            (Kind.STRING, "esc\"ape"),
            (Kind.CL_BRACKET, "]"),
            (Kind.CL_BRACE, "}"),
        ]

        source = '{"hello": "world","foo":["bar", 12.53, true, false, "esc\\"ape"]}'
        lexer = Lexer(source)

        for kind, literal in tokens:
            token = lexer.next_token()

            self.assertEqual(kind, token.kind)
            self.assertEqual(literal, token.literal)
