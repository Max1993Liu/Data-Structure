from BinaryTree import *
from MapBase import * 

class TreeMap(LinkedBinaryTree, MapBase):

	class Position(LinkedBinaryTree.Position):
		def key(self):
			return self.element()._key

		def value(self):
			return self.element()._value

	def _subtree_search(self, p, k):
		if p.key() == k:
			return p
		elif k < p.key():
			if self.left(p):
				return self._subtree_search(self.left(p), k)
		else:
			if self.right(p):
				return self._subtree_search(self.right(p), k)
		return p

	def _subtree_first_position(self, p):
		walk = p
		while self.left(walk):
			walk = self.left(walk)
		return walk

	def _subtree_last_position(self, p):
		walk = p
		while self.right(p):
			walk = self.right(walk)
		return walk

	def first(self):
		return self._subtree_first_position(self.root()) if len(self) > 0 else None

	def last(self):
		return self._subtree_last_position(self.root()) if len(self) > 0 else None

	def before(self, p):
		self._validate(p)
		if self.left(p):
			return self._subtree_last_position(self.left(p))
		else:
			walk = p
			ancestor = self.parent(walk)
			while ancestor and walk == self.left(ancestor):
				walk = ancestor
				ancestor = self.parent(walk)
			return ancestor

	def after(self, p):
		self._validate(p)
		if self.right(p):
			return self._subtree_first_position(self.right(p))
		else:
			walk = p 
			ancestor = self.parent(walk)
			while ancestor and walk == self.right(ancestor):
				walk = ancestor
				ancestor = self.parent(walk)
			return ancestor

	def find_position(self, k):
		if self.is_empty():
			return None
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			return p

	def find_min(self):
		if self.is_empty():
			return None
		else:
			p = self.first()
			return (p.key(), p.value())

	def find_ge(self, k):
		if self.is_empty():
			return None
		else:
			p = self.find_position(k)
			if p.key() != k:
				p = self.after(p)
			return (p.key(), p.value())

	def find_range(self, start, stop):
		if not self.is_empty():
			if start is None:
				p = self.first()
			else:
				p = self.find_position(start)
				if p.key() < start:
					p = self.after(p)
			while p is not None and (stop is None or p.key() < stop):
				yield (p.key(), p.value())
				p = self.after(p)

	def delete(self, p):
    """Remove the item at given Position."""
    self._validate(p)                            # inherited from LinkedBinaryTree
    if self.left(p) and self.right(p):           # p has two children
      replacement = self._subtree_last_position(self.left(p))
      self._replace(p, replacement.element())    # from LinkedBinaryTree
      p =  replacement
    # now p has at most one child
    parent = self.parent(p)
    self._delete(p)                              # inherited from LinkedBinaryTree
    self._rebalance_delete(parent)               # if root deleted, parent is None
      
  #--------------------- public methods for (standard) map interface ---------------------
  def __getitem__(self, k):
    """Return value associated with key k (raise KeyError if not found)."""
    if self.is_empty():
      raise KeyError('Key Error: ' + repr(k))
    else:
      p = self._subtree_search(self.root(), k)
      self._rebalance_access(p)                  # hook for balanced tree subclasses
      if k != p.key():
        raise KeyError('Key Error: ' + repr(k))
      return p.value()

  def __setitem__(self, k, v):
    """Assign value v to key k, overwriting existing value if present."""
    if self.is_empty():
      leaf = self._add_root(self._Item(k,v))     # from LinkedBinaryTree
    else:
      p = self._subtree_search(self.root(), k)
      if p.key() == k:
        p.element()._value = v                   # replace existing item's value
        self._rebalance_access(p)                # hook for balanced tree subclasses
        return
      else:
        item = self._Item(k,v)
        if p.key() < k:
          leaf = self._add_right(p, item)        # inherited from LinkedBinaryTree
        else:
          leaf = self._add_left(p, item)         # inherited from LinkedBinaryTree
    self._rebalance_insert(leaf)                 # hook for balanced tree subclasses

  def __delitem__(self, k):
    """Remove item associated with key k (raise KeyError if not found)."""
    if not self.is_empty():
      p = self._subtree_search(self.root(), k)
      if k == p.key():
        self.delete(p)                           # rely on positional version
        return                                   # successful deletion complete
      self._rebalance_access(p)                  # hook for balanced tree subclasses
    raise KeyError('Key Error: ' + repr(k))

  def __iter__(self):
    """Generate an iteration of all keys in the map in order."""
    p = self.first()
    while p is not None:
      yield p.key()
      p = self.after(p)



