from BaseTree import *
#deque for bfs
from collections import deque

class BinaryTree(Tree):

	def left(self, p):
		raise NotImplementedError

	def right(self,p):
		raise NotImplementedError

	def sibling(self, p):
		parent = self.parent(p)
		if parent is None:
			return None
		else:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)

	def children(self, p):
		if self.left(p):
			yield self.left(p)
		if self.right(p):
			yield self.right(p)


class LinkedBinaryTree(BinaryTree):

	class _Node(object):
		__slots__ = '_element', '_parent', '_left', '_right'
		def __init__(self, element, parent = None, left = None, right = None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right


	class Position(BinaryTree.Position):

		def __init__(self, container, node):
			self._container = container
			self._node = node

		def element(self):
			return self._node._element

		def __eq__(self, other):
			return type(other) is type(self) and other._node is self._node

		def __ne__(self, other):
			return not (self == other)

	def _validate(self, p):
		if not isinstance(p, self.Position):
			raise TypeError
		if p._container is not self:
			raise ValueError
		if p._node._parent == p._node:
			raise ValueError
		return p._node

	def _make_position(self, node):
		return self.Position(self, node) if node is not None else None

	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		return self._size

	def root(self):
		return self._make_position(self._root)

	def parent(self, p):
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		node = self._validate(p)
		count = 0 
		if self._left:
			count += 1
		if self._right:
			count += 1
		return count

	def _add_root(self, e):
		if self._root is not None:
			raise ValueError
		new_node = self._Node(e)
		self._size = 1
		self._root = new_node
		return self._make_position(new_node)

	def _add_left(self, p, e):
		node = self._validate(p)
		if node._left is not None:
			raise ValueError
		self._size += 1
		new_node = self._Node(e, node)
		node._left = new_node
		return self._make_position(node._left)

	def _add_right(self, p, e):
		node = self._validate(p)
		if node._right is not None:
			raise ValueError
		self._size += 1
		new_node = self._Node(e, node)
		node._right = new_node
		return self._make_position(node._right)

	def _replace(self, p, e):
		node = self._validate(p)
		old = node._element
		node._element = e
		return old

	def _delete(self, p):
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError
		child_node = node._left if node._left else node._right
		if child_node:
			child_node._parent = node._parent
		if node is self._root:
			self._root = child_node
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child_node
			else:
				parent._right = child_node
		self._size -= 1
		node._parent = node
		return node._element

	def __iter__(self):
		for p in self.positions():
			yield p.element()

	def preorder(self, p):
		if p:
			yield p
			for child in self.children(p):
				 for x in self.preorder(child):
				 	yield x 


	def postorder(self, p):
		for child in self.children(p):
			for x in self.preorder(child):
				yield x
		yield p 

	def positions(self):
		return self.inorder(self.root())

	def bfs(self):
		if not self.is_empty():
			fringe = deque()
			fringe.bappend(self.root())
			while len(fringe) > 0:
				p = fringe.popleft()
				yield p
				for child in self.children(p):
					fringe.append(child)

	def inorder(self, p):
		if self.left(p):
			for x in self.inorder(self.left(p)):
				yield x
		yield p
		if self.right(p):
			for x in self.inorder(self.right(p)):
				yield x

	def _indent(self, p):
		depth = self.depth(p)
		print 2 * depth * ' ' + str(p.element())
		for child in self.children(p):
			self._indent(child)

	def preorder_indent(self):
		self._indent(self.root())

	def _indent_index(self, p, path):
		depth = self.depth(p)
		if self.parent(p):
			parent = self.parent(p)
			if p is self.left(parent):
				path.append(1)
			else:
				path.append(2)
		print path
		print '.'.join(path)
		
		print '.'.join(path) , 2*depth*' ' , str(p.element()) 
		for child in self.children(p):
			self._indent_index(child, path)

	def preorder_index_indent(self):
		self._indent_index(self.root(), [])

t = LinkedBinaryTree()
root = t._add_root('Paper')
left = t._add_left(root, 'Chapter one')
right = t._add_right(root, 'Chapter two')
t._add_left(left,'One A')
t._add_right(left,'One B')
t._add_left(right, 'Two A')
t._add_right(right, 'Two B')
#for i in t:
#	print i
t.preorder_index_indent()
