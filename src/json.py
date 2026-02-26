from src.lexer import Lexer
from src.parser import Parser
from src.ast import ArrayAST, ObjectAST


def __to_array(ast: ArrayAST):
    arr = []
    for item in ast.items:
        arr.append(__to_python_data(item))
    return arr


def __to_object(ast: ObjectAST):
    obj = {}
    for key, val in zip(ast.keys, ast.values):
        obj[key] = __to_python_data(val)
    return obj


def __to_python_data(ast):
    match ast:
        case str() | float() | bool(): return ast
        case ArrayAST(): return __to_array(ast)
        case ObjectAST(): return __to_object(ast)
        case _: raise ValueError(f"json: unkown value {ast}")


def parse(source: str):
    lexer = Lexer(source)
    parser = Parser(lexer)

    return __to_python_data(parser.parse())
