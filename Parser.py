from Lex import Lex
from Node import Node
import TokenType
import re

#TODO: Add exception handling for if we run out of lexemes. That will handle som errors

class Parser:
	def __init__(self, fn):
		self.lex = Lex(fn)
		self.parse()
		self.headNode.out()

	def parse(self):
		tok = self.lex.tokens.pop(0)
		self.match(tok, TokenType.ot)
		name = self.lex.tokens.pop(0)
		attributes = self.getAttributes()
		self.match(self.lex.tokens.pop(0), TokenType.ct) # Should have a close tag here
		self.headNode = Node(name, attributes)
		self.getChildren(self.headNode)
		
	def getAttributes(self):
		attributes = {}
		tok = self.lex.tokens[0]
		while tok != '>' and tok != '/>':
			key = self.lex.tokens.pop(0)
			tok = self.lex.tokens.pop(0)
			#print("ket: " + key)
			#print(tok)
			if tok == '=':
				tok = self.lex.tokens.pop(0)
				val = tok
				attributes[key] = tok
			else:
				print("Unexpected token: " + tok)
				exit(1)
			tok = self.lex.tokens[0]

		return attributes

	def getChildren(self, node):
		tok = self.lex.tokens.pop(0)
		self.match(tok, TokenType.ot)
		while tok != '</':
			name = self.lex.tokens.pop(0)
			attributes = self.getAttributes()
			n = Node(name, attributes)
			node.children.append(n)
			tok = self.lex.tokens.pop(0)
			if tok == '>':
				self.getChildren(n)
			elif tok == '/>':
				pass
			else:
				print('Unexpected token: ' + tok)
				exit(1)
			tok = self.lex.tokens.pop(0)
		tok = self.lex.tokens.pop(0)
		if tok != node.tag:
			print ("Missmatch close tag: " + tok)
			exit(1)
		self.match(self.lex.tokens.pop(0), TokenType.ct)

	def match(self, tok, tokType):
		if tokType.match(tok):
			pass
		else:
			print("Invalid token: " + tok)
			exit(1)

if __name__ == '__main__':
	p = Parser('sample.xml')
