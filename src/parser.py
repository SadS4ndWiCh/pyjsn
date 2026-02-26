from src.lexer import Lexer
from src.token import Kind, Token
from src.ast import ObjectAST


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.curr_token: Token = None

    def next_token(self):
        self.curr_token = self.lexer.next_token()
        return self.curr_token

    def advance_expected_token(self, kind: Kind):
        if self.curr_token.kind != kind:
            return False

        self.next_token()
        return True

    def parse_object(self) -> ObjectAST:
        ast = ObjectAST()

        while self.curr_token.kind != Kind.CL_BRACE:
            key = self.next_token()
            if not self.advance_expected_token(Kind.STRING):
                return None

            if not self.curr_token.kind == Kind.COLON:
                return None

            ast.keys.append(key.literal)
            ast.values.append(self.parse())

            self.next_token()
            if self.curr_token.kind != Kind.CL_BRACE and self.curr_token.kind != Kind.COMMA:
                return None

        return ast

    def parse(self):
        match (token := self.next_token()).kind:
            case Kind.OP_BRACE: return self.parse_object()
            case Kind.STRING: return token.literal
            case _: return None
