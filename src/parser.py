from src.tokens import Tokens

class Parser:
	def __init__(self, lex):
		self.lex = lex
		self.errors = []
		
		self.currToken = None
		self.peekToken = None
		
		self._nextToken()
		self._nextToken()
	
	def _currTokenIs(self, tk): return self.currToken.type == tk
	def _peekTokenIs(self, tk): return self.peekToken.type == tk
	def _expectPeek(self, tk):
		if self._peekTokenIs(tk):
			self._nextToken()
			return True
		
		self.errors.append(f"Expect {tk}, got={self.peekToken.type}")
		return False
	
	def _nextToken(self):
		self.currToken = self.peekToken
		self.peekToken = self.lex.nextToken()
	
	def _parseObject(self):
		obj = {}
		
		while not self._currTokenIs(Tokens.CLBRACE) and \
					not self._currTokenIs(Tokens.EOF):
			if not self._expectPeek(Tokens.STRING): return None
		
			key = self.currToken.literal
			
			if not self._expectPeek(Tokens.COLON): return None
			
			self._nextToken()
			
			obj[key] = self._parse()
			
			self._nextToken()
			
		return obj
	
	def _parse(self):
		tok = self.currToken
		
		if self._currTokenIs(Tokens.TRUE): return True
		elif self._currTokenIs(Tokens.FALSE): return False
		elif self._currTokenIs(Tokens.STRING): return tok.literal
		elif self._currTokenIs(Tokens.OPBRACE):
			return self._parseObject()
		elif self._currTokenIs(Tokens.NUMBER): return float(tok.literal)
			
	
	def parse(self):
		return self._parse()

