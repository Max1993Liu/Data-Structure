from PositionalList import PositionalList
class Empty(Exception):
	pass


class PriorityQueueBase:

	class _Item:
		__slots__ = '_key', '_value'

		def __init__(self, key, value):
			self._key = key
			self._value = value

		def __lt__(self, other):
			return self._key < other._key

		def __gt__(self, other):
			return not self < other

	def is_empty(self):
		return len(self) == 0 

class UnsortedPriorityQueue(PriorityQueueBase):
	MINIMUM = None

	def _find_min(self):
		if self.is_empty():
			raise Empty('Priority queue is empty')
		else:
			minimum = self._data.first()
			walker = self._data.after(minimum)
			while walker is not None:
				if walker.element() < minimum.element():
					minimum = walker
				walker = self._data.after(walker)
		return minimum

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self, key, value):
		if len(self) == 0:
			self.MINIMUM = (key, value)
		else:
			if key < self.MINIMUM[0]:
				self.MINIMUM = (key, value)
		self._data.add_last(self._Item(key, value))

	def min(self):
		#p is a position
		p = self._find_min()
		item = p.element()
		return (item._key, item._value)

	def remove_min(self):
		#item = self._data.delete(self._find_min())
		#return (item._key, item_value)
		return MINIMUM

	def __repr__(self):
		res = []
		walk = self._data.first()
		while walk is not None:
			res.append((walk.element()._key, walk.element()._value))
			walk = self._data.after(walk)
		return str(res)



class SortedPriorityQueue(PriorityQueueBase):

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self, key, value):
		new = self._Item(key, value)
		walk = self._data.last()
		while walk is not None and new < walk.element():
			walk = self._data.before(walk)
		if walk is None:
			self._data.add_first(new)
		else:
			self._data.add_after(walk, new)

	def min(self):
		if self.is_empty():
			return Empty('empty')
		p = self._data.first()
		item = p.element()
		return (item._key, item._value)

	def remove_min(self):
		if self.is_empty():
			raise Empty('empty')
		item = self._data.delete(self._data.first())
		return (item._key, item._value)
