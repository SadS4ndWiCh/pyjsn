from enum import Enum


class Kind(Enum):
    EOF = "EOF"
    UNKNOWN = "UNKNOWN"
    INVALID = "INVALID"

    OP_BRACE = "OP_BRACE"
    CL_BRACE = "CL_BRACE"
    OP_BRACKET = "OP_BRACKET"
    CL_BRACKET = "CL_BRACKET"

    COLON = "COLON"
    COMMA = "COMMA"

    STRING = "STRING"
    NUMBER = "NUMBER"
    TRUE = "TRUE"
    FALSE = "FALSE"


class Token:
    def __init__(self, kind: Kind, literal: str):
        self.kind = kind
        self.literal = literal

    @staticmethod
    def from_ident(ident: str) -> "Token":
        match ident:
            case "true": return Token(Kind.TRUE, ident)
            case "false": return Token(Kind.FALSE, ident)
            case _: return Token(Kind.UNKNOWN, ident)
