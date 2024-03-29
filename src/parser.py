from src.tokens import Tokens


class Parser:
    def __init__(self, lex):
        self.lex = lex
        self.errors = []

        self.curr_token = None
        self.peek_token = None

        self.__next_token()
        self.__next_token()

    def __add_error(self, error):
        self.errors.append(error)

    def __curr_token_is(self, tk):
        return self.curr_token.type == tk

    def __peek_token_is(self, tk):
        return self.peek_token.type == tk

    def __expect_peek(self, tk):
        if self.__peek_token_is(tk):
            self.__next_token()
            return True

        self.__add_error(f"Expect {tk}, got={self.peek_token.type}")
        return False

    def __next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lex.next_token()

    def __parse_object(self):
        obj = {}

        while not self.__curr_token_is(Tokens.CLBRACE) and not self.__curr_token_is(
            Tokens.EOF
        ):
            if not self.__expect_peek(Tokens.STRING):
                return None

            key = self.curr_token.literal

            if not self.__expect_peek(Tokens.COLON):
                return None

            self.__next_token()

            obj[key] = self.__parse()

            self.__next_token()

        return obj

    def __parse_array(self):
        arr = []

        self.__next_token()

        while not self.__curr_token_is(Tokens.CLBRACKET) and not self.__curr_token_is(
            Tokens.EOF
        ):
            if self.__curr_token_is(Tokens.COMMA) and self.__peek_token_is(
                Tokens.CLBRACKET
            ):
                self.__add_error("Expected value, got=CLBRACKET")
                return None

            elif self.__curr_token_is(Tokens.COMMA):
                self.__next_token()
                continue

            element = self.__parse()
            arr.append(element)

            self.__next_token()

        return arr

    def __parse(self):
        tok = self.curr_token

        if self.__curr_token_is(Tokens.TRUE):
            return True
        elif self.__curr_token_is(Tokens.FALSE):
            return False
        elif self.__curr_token_is(Tokens.STRING):
            return tok.literal
        elif self.__curr_token_is(Tokens.OPBRACE):
            return self.__parse_object()
        elif self.__curr_token_is(Tokens.OPBRACKET):
            return self.__parse_array()
        elif self.__curr_token_is(Tokens.NUMBER):
            return float(tok.literal)

    def parse(self):
        return self.__parse()
