from src.tokens import Tokens, Token, lookupIdent

class Lexer:
    tokens = {
        "{": Token(Tokens.OPBRACE, "{"),
        "}": Token(Tokens.CLBRACE, "}"),
        "[": Token(Tokens.OPBRACKET, "["),
        "]": Token(Tokens.CLBRACKET, "]"),
        ":": Token(Tokens.COLON, ":"),
        ",": Token(Tokens.COMMA, ",")
    }

    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.nextPos = 0
        self.ch = None

        self._readChar()

    def _readChar(self):
        if self.nextPos >= len(self.input):
            self.ch = None
            return

        self.pos = self.nextPos
        self.ch = self.input[self.pos]
        self.nextPos += 1

    def _isText(self, ch):
        return ch != '"' and ch != "\n"

    def _isIdent(self, ch):
        return ch in "abcdefghijklmniopqrstuvwxyz"

    def _isDigit(self, ch):
        return ch in "0123456789."

    def _getText(self):
        self._readChar()
        pos = self.pos

        while self._isText(self.ch):
            self._readChar()

        text = self.input[pos:self.pos]
        self._readChar()

        return text

    def _getIdent(self):
        pos = self.pos

        while self._isIdent(self.ch):
            self._readChar()

        ident = self.input[pos:self.pos]

        return ident

    def _getDigit(self):
        pos = self.pos

        while self._isDigit(self.ch):
            self._readChar()

        digit = self.input[pos:self.pos]

        return digit

    def _eatWhitespace(self):
        while self.ch in [" ", "\n", "\t", "\r"]:
            self._readChar()

    def nextToken(self):
        self._eatWhitespace()

        ch = self.ch
        tok = Token(Tokens.INVALID, None)

        if ch in Lexer.tokens:
            tok = Lexer.tokens[ch]

        elif ch == '"':
            tok = Token(Tokens.STRING, self._getText())
            return tok

        elif ( not ch is None ) and self._isDigit(self.ch):
            digit = self._getDigit()

            tok = Token(Tokens.NUMBER, digit)
            return tok

        elif ( not ch is None ) and self._isIdent(self.ch):
            ident = self._getIdent()

            tok = Token(lookupIdent(ident), ident)
            return tok

        elif ch is None:
            tok = Token(Tokens.EOF, "")

        self._readChar()
        return tok

