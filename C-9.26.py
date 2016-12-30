#implement stack with priority queue
from Heap import * 

class PriorityQueueStack(HeapPriorityQueue):
	INDEX = 0

	def add(self, value):
		self._data.append(self._Item(self.INDEX, value))
		self._upheap(len(self._data) - 1)
		self.INDEX -= 1


t = PriorityQueueStack()
t.add(2)
t.add(5)
t.add(9)
t.min()

		