from collections import MutableMapping

class MapBase(MutableMapping):

	class _Item(object):
		__slots__ = '_key','_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __eq__(self, other):
			return self._key == other._key

		def __ne__(self, other):
			return not (self == other)

		def __lt__(self, other):
			return self._key < other._key

		



class UnsortedTableMap(MapBase):

	def __init__(self):
		self._table = []

	def __getitem__(self, k):
		for i in self._table:
			if i._key == k:
				return i._value

		raise KeyError('Not Found')

	def __setitem__(self, k, v):
		for i in self._table:
			if i._key == k:
				i._value = v
				return
		self._table.append(self._Item(k,v))

	def __delitem__(self, k):
		for i in range(len(self._table)):
			if self._table[i]._key == k:
				self._table.pop(i)
				return
		raise KeyError('Not Found!')

	def __len__(self):
		return len(self._table)

	#yield the key, not the value
	def __iter__(self):
		for i in self._table:
			yield i._key

	def __str__(self):
		res = []
		for i in self._table:
			res.append(i._value)
		return str(' '.join(res))

	def setdefault(self, k, v):
		if len(self._table) == 0:
			self._table.append(self._Item(k,v))
		else:
			for i in self._table:
				if i._key == k:
					return i._value
			self._table.append(self._Item(k,v))
			return v



s = UnsortedTableMap()
s[1] = 'a'
s[2] = 'b'
s[3] = 'c'
