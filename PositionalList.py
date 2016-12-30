from DoublyLinkedList import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

	#nested class
	class Position:

		def __init__(self, container, node):
			self._container = container
			self._node = node

		def element(self):
			return self._node._element

		def __eq__(self, other):
			return type(self) is type(other) and type._node is other._node

		def __ne__(self, other):
			return not (self == other)

	#------------------utility functions----------------
	def _validate(self, p):
		#return position's node if it's valid
		if not isinstance(p, self.Position):
			raise TypeError('p must be a position!')

		if p._container is not self:
			raise ValueError('p does not belong to this container!')

		if p._node._next is None:
			raise ValueErrr('p is no longer valid!')

		return p._node

	def _make_position(self, node):
		if node is self._header or node is self._trailer:
			return None
		else:
			return self.Position(self, node)

	#-------------------accessors------------------------
	def first(self):
		return self._make_position(self._header._next)

	def last(self):
		return self._make_position(self._trailer._prev)

	def before(self, p):
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self, p):
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)

	def _insert_between(self, e, predecessor, successor):
		node = super(PositionalList, self)._insert_between(e, predecessor, successor)
		return self._make_position(node)

	def add_first(self, e):
		return self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		return self._insert_between(e, self._trailer._prev, self._trailer)

	def add_before(self, p, e):
		original = self._validate(p)
		return self._insert_between(e, original._prev, original)

	def add_after(self, p, e):
		original = self._validate(p)
		return self._insert_between(e, original, original._next)

	def delete(self, p):
		original = self._validate(p)
		return self._delete_node(original)

	def replace(self, p, e):
		original = self._validate(p)
		old_value = original._element
		original.element = e
		return old_value
		