import sys
class Node(object):
	def __init__(self, tag, data=None):
		self.tag = tag
		self.data = data
		self.children = list()
	def out(self, tabs=0):
		for i in range(tabs):
			sys.stdout.write("\t")
		print(self.tag + ": " + str(self.data))
		for i in self.children:
			i.out(tabs+1)

if __name__ == '__main__':
	head = Node('root', 'this')
	head.children.append(Node("node", "data"))
	c = Node("node", "that")
	c.children.append(Node("node2", "inside"))
	head.children.append(c)

	head.out()
