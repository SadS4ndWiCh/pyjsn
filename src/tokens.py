from enum import Enum
from dataclasses import dataclass

class Tokens(Enum):
	INVALID = "INVALID"
	EOF     = "EOF"
	
	OPBRACE   = "OPBRACE"
	CLBRACE   = "CLBRACE"
	OPBRACKET = "OPBRACKET"
	CLBRACKET = "CLBRACKET"
	COMMA     = "COMMA"
	COLON     = "COLON"
	
	
	TRUE   = "TRUE"
	FALSE  = "FALSE"
	STRING = "STRING"
	NUMBER = "NUMBER"

keywords = {
	"true": Tokens.TRUE,
	"false": Tokens.FALSE
}


def lookupIdent(ident):
        if ident in keywords:
                return keywords[ident]
        
        return ident


@dataclass
class Token:
	type: Tokens
	literal: str
