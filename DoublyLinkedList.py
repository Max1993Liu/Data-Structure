class Empty(Exception):
	pass


class _DoublyLinkedBase(object):

	class _Node:
		__slots__ = '_element', '_prev', '_next'

		def __init__(self, element, prev_node, next_node):
			self._element = element
			self._prev = prev_node
			self._next = next_node

	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._size = 0
		self._header._next = self._trailer
		self._trailer._prev = self._header

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		new_node = self._Node(e, predecessor, successor)
		predecessor._next = new_node
		successor._prev = new_node
		self._size += 1
		#return the newly created node
		return new_node

	def _delete_node(self, node):
		predecessor, successor = node._prev, node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		#return deleted element
		element  = node._element
		node._prev = node._next = node._element = None
		return element


class LinkedDeque(_DoublyLinkedBase):

	def first(self):
		if self.is_empty():
			raise Empty('Deque is empty')
		else:
			return self._header._next._element

	def last(self):
		if self.is_empty():
			raise Empty('Deque is empty')
		else:
			return self._trailer._prev._element


	def insert_first(self, e):
		self._insert_between(e, self._header, self._header._next)

	def insert_last(self, e):
		self._insert_between(e, self._trailer._prev, self._trailer)

	def delete_first(self):
		if self.is_empty():
			raise Empty('Deque is empty')
		else:
			self._delete_node(self._header._next)

	def delete_last(self):
		if self.is_empty():
			raise Empty('Deque is empty')
		else:
			self._delete_node(self._trailer._prev)

#t = LinkedDeque()
#t.delete_first()


