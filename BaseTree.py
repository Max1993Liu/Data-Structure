#Implementation for base tree class

class Tree(object):
	
	class Position(object):
		def element(self):
			raise NotImplementedError

		def __eq__(self, other):
			raise NotImplementedError

		def __ne__(self, other):
			return not (self == other)

	def root(self):
		raise NotImplementedError

	def parent(self, p):
		raise NotImplementedError

	def num_children(self, p):
		raise NotImplementedError

	def children(self, p):
		raise NotImplementedError

	def __len__(self):
		raise NotImplementedError

	def is_root(self, p):
		return self.parent(p) == None

	def is_leaf(self, p):
		raise NotImplementedError

	def is_empty(self):
		return len(self) == 0

	def depth(self, p):
		if self.is_root(p):
			return 0
		else:
			return 1 + self.depth(self.parent(p))

	def height(self, p = None):
		if p is None:
			p = self.root()
		if self.is_leaf(p):
			return 0
		else:
			return 1 + max(self.height(i) for i in self.children(p))




