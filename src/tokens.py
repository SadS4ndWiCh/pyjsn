from enum import Enum
from dataclasses import dataclass


class Tokens(Enum):
    INVALID = "INVALID"
    EOF = "EOF"

    OPBRACE = "OPBRACE"
    CLBRACE = "CLBRACE"
    OPBRACKET = "OPBRACKET"
    CLBRACKET = "CLBRACKET"
    COMMA = "COMMA"
    COLON = "COLON"

    TRUE = "TRUE"
    FALSE = "FALSE"
    STRING = "STRING"
    NUMBER = "NUMBER"


@dataclass
class Token:
    type: Tokens
    literal: str


keywords = {"true": Tokens.TRUE, "false": Tokens.FALSE}


def lookup_ident(ident):
    if ident in keywords:
        return keywords[ident]

    return ident
