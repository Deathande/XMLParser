import string
import re

class Lex:
	def __init__(self, fn):
		f = open(fn, 'r')
		self.tokens = list()
		for line in f:
			self.procLine(line)

	def procLine(self, line):
		i = self.skipWhitespace(line, 0)
		while i < len(line):
			i = self.getLexeme(line, i)
			i = self.skipWhitespace(line, i)
	
	def skipWhitespace(self, line, i):
		reg = re.compile('\s')
		if reg.match(line[i]):
			while i < len(line) and reg.match(line[i]):
				i += 1
		return i
			
	def getLexeme(self, line, index ):
		if line[index] == '<':
			if (line[index+1] == '/'):
				self.tokens.append('</')
				return index+2
			self.tokens.append('<')
			return index+1
		elif re.match('\w', line[index]):
			reg = re.compile('\w')
			word = ''
			while index < len(line) and reg.match(line[index]):
				word +=line[index]
				index += 1
			self.tokens.append(word)
			return index
		elif line[index] == '"':
			reg = re.compile('\w|\s')
			word = ''
			if line[index+1] == '"':
				self.tokens.append(word)
				return index + 2
			index += 1
			while index < len(line) and reg.match(line[index]):
				word += line[index]
				index += 1
			self.tokens.append(word)
			return index+1
				
		elif re.match('>', line[index]):
			self.tokens.append('>')
			return index + 1
		elif line[index] == '=':
			self.tokens.append('=')
			return index + 1

		elif re.match('/', line[index]):
			reg1 = re.compile('>')
			reg2 = re.compile('\w')
			if reg1.match(line[index+1]):
				self.tokens.append('/>')
				return index + 2
			elif reg2.match(line[index+1]): # The hell were you thinking?
				self.tokens.append('</')
				return index+1
			else:
				print('Unexpected token: ' + line[index+1])
				exit(1)
		else:
			print('Unexpected token: ' + line[index])
			exit(1)

if __name__ == '__main__':
	l = Lex('sample.xml')
