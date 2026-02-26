from src.token import Kind, Token


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.len = len(source)
        self.cur = 0
        self.ch = None

    def read_char(self) -> str:
        if self.cur >= self.len:
            return ""

        self.ch = self.source[self.cur]
        self.cur += 1
        return self.ch

    def seek_char(self) -> str:
        if self.cur >= self.len:
            return ""

        return self.source[self.cur]

    def eat_space(self) -> None:
        while self.seek_char().isspace():
            self.read_char()

    def read_ident(self) -> str:
        start = self.cur
        while self.seek_char().isalpha():
            self.read_char()
        end = self.cur
        return self.source[start-1:end]

    def read_string(self) -> str:
        text = ""
        while (ch := self.read_char()) != "\"":
            if ch == "\\":
                self.read_char()
            text += self.ch
        return text

    def read_number(self) -> float:
        start = self.cur
        dot = False
        while (ch := self.seek_char()).isnumeric() or ch == ".":
            if ch == ".":
                if dot:
                    break
                dot = True
            self.read_char()
        end = self.cur
        return self.source[start-1:end]

    def next_token(self) -> Token:
        self.eat_space()

        match ch := self.read_char():
            case "{": return Token(Kind.OP_BRACE, ch)
            case "}": return Token(Kind.CL_BRACE, ch)
            case "[": return Token(Kind.OP_BRACKET, ch)
            case "]": return Token(Kind.CL_BRACKET, ch)
            case ":": return Token(Kind.COLON, ch)
            case ",": return Token(Kind.COMMA, ch)
            case "\"": return Token(Kind.STRING, self.read_string())
            case "": return Token(Kind.EOF, ch)
            case _:
                if ch.isnumeric():
                    return Token(Kind.NUMBER, self.read_number())

                if ch.isalpha():
                    return Token.from_ident(self.read_ident())

                return Token(Kind.UNKNOWN, ch)
