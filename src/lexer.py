from src.tokens import Tokens, Token, lookup_ident


class Lexer:
    tokens = {
        "{": Token(Tokens.OPBRACE, "{"),
        "}": Token(Tokens.CLBRACE, "}"),
        "[": Token(Tokens.OPBRACKET, "["),
        "]": Token(Tokens.CLBRACKET, "]"),
        ":": Token(Tokens.COLON, ":"),
        ",": Token(Tokens.COMMA, ","),
    }

    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.next_pos = 0
        self.ch = None

        self.__read_char()

    def __read_char(self):
        if self.next_pos >= len(self.input):
            self.ch = None
            return

        self.pos = self.next_pos
        self.ch = self.input[self.pos]
        self.next_pos += 1

    def __is_text(self, ch):
        return ch != '"' and ch != "\n"

    def __is_ident(self, ch):
        return ch in "abcdefghijklmniopqrstuvwxyz"

    def __is_digit(self, ch):
        return ch in "0123456789."

    def __get_text(self):
        self.__read_char()
        pos = self.pos

        while self.__is_text(self.ch):
            self.__read_char()

        text = self.input[pos : self.pos]
        self.__read_char()

        return text

    def __get_ident(self):
        pos = self.pos

        while self.__is_ident(self.ch):
            self.__read_char()

        ident = self.input[pos : self.pos]

        return ident

    def __get_digit(self):
        pos = self.pos

        while self.__is_digit(self.ch):
            self.__read_char()

        digit = self.input[pos : self.pos]

        return digit

    def __eat_whitespace(self):
        while self.ch in [" ", "\n", "\t", "\r"]:
            self.__read_char()

    def next_token(self):
        self.__eat_whitespace()

        ch = self.ch

        if ch is None:
            tok = Token(Tokens.EOF, "")

        elif ch in Lexer.tokens:
            tok = Lexer.tokens[ch]

        elif ch == '"':
            tok = Token(Tokens.STRING, self.__get_text())
            return tok

        elif self.__is_digit(self.ch):
            tok = Token(Tokens.NUMBER, self.__get_digit())
            return tok

        elif self.__is_ident(self.ch):
            ident = self.__get_ident()

            tok = Token(lookup_ident(ident), ident)
            return tok

        else:
            tok = Token(Tokens.INVALID, None)

        self.__read_char()
        return tok
