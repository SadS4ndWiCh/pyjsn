from src.lexer import Lexer
from src.parser import Parser

if __name__ == "__main__":
	inp = '{"test": ["aaaaa", 23, false, { "some": "ohhh" }]}'
	
	lex = Lexer(inp)
	json = Parser(lex)
	
	data = json.parse()
	
	print(data)
	print(json.errors)

