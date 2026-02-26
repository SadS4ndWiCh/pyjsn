from enum import Enum


class KindAST(Enum):
    OBJECT = "OBJECT"
    ARRAY = "ARRAY"


class AbstractAST:
    def __init__(self, kind: KindAST):
        self.kind = kind


class ObjectAST(AbstractAST):
    def __init__(self):
        super().__init__(KindAST.OBJECT)

        self.keys = []
        self.values = []


class ArrayAST(AbstractAST):
    def __init__(self):
        super().__init__(KindAST.ARRAY)

        self.items = []
