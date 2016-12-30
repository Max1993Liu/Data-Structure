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


class SortedPriorityQueue(PriorityQueueBase):

	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def _pushForward(self, j):
		if j > 0 and self._data[j] < self._data[j-1]:
			self._data[j], self._data[j-1] = self._data[j-1], self._data[j]
			self._pushForward(j - 1)

	def add(self, key, value):
		new_item = self._Item(key, value)
		self._data.append(new_item)
		self._pushForward(len(self) - 1)

	def min(self):
		item = self._data[0]
		return (item._key, item._value)

	def remove_min(self):
		item = self._data.pop(0)
		return (item._key, item._value)

t = SortedPriorityQueue()
t.add(2,3)
t.add(3,5)
t.add(1,3)
t.add(19,2)
print(t.min())
	
