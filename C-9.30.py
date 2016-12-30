while j > 0 and self._data[j] < self._data[self._parent(j)]:
			self._swap(j, self._parent(j))
			j = self._parent(j)
