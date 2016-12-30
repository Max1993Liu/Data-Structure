#Heap for priority queue

class PriorityQueueBase(object):

	class _Item(object):
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


class HeapPriorityQueue(PriorityQueueBase):

	def _parent(self, j):
		return (j-1) // 2

	def _left(self, j):
		res = 2 * j + 1
		return res if res < len(self._data) else None

	def _right(self, j):
		res = 2 * j + 2
		return res if res < len(self._data) else None

	def _swap(self, i, j):
		self._data[i], self._data[j] = self._data[j], self._data[i]

	def _upheap(self, j):
		parent = self._parent(j)
		if j > 0 and self._data[j] < self._data[parent]:
			self._swap(j, parent)
			#recursion
			self._upheap(parent)
		
		#while j > 0 and self._data[j] < self._data[self._parent(j)]:
		#	self._swap(j, self._parent(j))
		#	j = self._parent(j)


	def _downheap(self, j):
		if self._left(j):
			left = self._left(j)
			small_child = left
			if self._right(j):
				right = self._right(j)
				if self._data[right] < self._data[left]:
					small_child = right
			if self._data[small_child] < self._data[j]:
				self._swap(j, small_child)
				self._downheap(small_child)

	def __init__(self, contents = ()):
		#in case there're exising contents
		self._data = [self._Item(k,v) for k,v in contents]
		if len(self._data) > 1:
			self._heapify()

	def _heapify(self):
		start = self._parent(len(self._data) -1)
		for i in range(start, -1, -1):
			self._downheap(i)

	def __len__(self):
		return len(self._data)
	
	def min(self):
		if self.is_empty():
			raise IndexError('Empty!')
		item = self._data[0]
		return (item._key, item._value)

	def remove_min(self):
		if self.is_empty():
			raise IndexError('Empty')	
		self._swap(0, len(self._data) -1)
		item = self._data.pop()
		self._downheap(0)
		return (item._key, item._value)

	def add(self, key, value):
		self._data.append(self._Item(key, value))
		self._upheap(len(self._data) - 1)


def hp_sort(C):
	n = len(C)
	H = HeapPriorityQueue()
	ret = []
	for i in range(n):
		H.add(C[i], C[i])
	for i  in range(n):
		#print H.min()[0]
		ret.append(H.remove_min()[0])
	return ret

t = HeapPriorityQueue()
t.add(0.5, 3)
t.add(9,3)
t.add(2,3)
t.add(1,6)
t.add(5,3)
print(t.min())