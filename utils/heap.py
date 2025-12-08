import heapq

class Heap:
  """min-heap with nicer interface"""
  def __init__(self, initial_data=None):
    if initial_data is None:
      self._data = []
    else:
      self._data = heapq.heapify(initial_data.copy())
  
  def push(self, item):
    heapq.heappush(self._data, item)

  def pop(self):
    return heapq.heappop(self)
  
  def __getitem__(self, key):
    return self._data[key]
