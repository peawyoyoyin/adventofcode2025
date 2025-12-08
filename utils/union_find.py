class UnionFind:
  def __init__(self, size: int):
    self._parent = { i:i for i in range(size) }
    self._unique_groups = set([i for i in range(size)])
    self._size = [1 for i in range(size)]
  
  def union(self, a: int, b: int):
    a = self.find_parent(a)
    b = self.find_parent(b)

    if self._size[a] < self._size[b]:
      a, b = b, a

    if a == b:
      return

    self._unique_groups.remove(b)
    self._parent[b] = a
    self._size[a] += self._size[b]

  def find_parent(self, a: int):
    if self._parent[a] == a:
      return a
    else:
      parent = self._parent[a]
      self._parent[a] = self.find_parent(parent)
      return self._parent[a]

  def unique_groups(self):
    return self._unique_groups

  def size(self, a: int):
    return self._size[self.find_parent(a)]
