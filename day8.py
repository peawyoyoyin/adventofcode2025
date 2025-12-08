from typing import List, Tuple
from utils.cli import run
from utils.union_find import UnionFind
from utils.heap import Heap

def parse_inputs(inputs: List[str]):
  result = []
  for line in inputs:
    t1, t2, t3 = line.strip().split(',')
    result.append((int(t1), int(t2), int(t3)))

  return result

# for comparisons, squaring is good enough
def dist2(p1: Tuple[int, int, int], p2: Tuple[int, int, int]):
  x1, y1, z1 = p1
  x2, y2, z2 = p2
  return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def part1(inputs: List[str]):
  points = parse_inputs(inputs)
  distances = Heap()
  for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
      if i >= j:
        continue
      distances.push((dist2(p1, p2), i, j))

  groups = UnionFind(len(inputs))
  
  connections = 1000 # this is 10 when running ex1

  while connections > 0:
    _dist, i, j = distances.pop()
    groups.union(i, j)
    connections -= 1
  
  sizes = Heap()
  for group in groups.unique_groups():
    group_size = groups.size(group)
    if len(sizes) < 3:
      sizes.push(group_size)
    elif group_size > sizes[0]:
      sizes.push(group_size)
      sizes.pop()

  result = 1
  for size in sizes:
    result *= size
  return result
  

def part2(inputs: List[str]):
  points = parse_inputs(inputs)
  distances = Heap()
  for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
      if i >= j:
        continue
      distances.push((dist2(p1, p2), i, j))

  groups = UnionFind(len(inputs))
  
  last_i, last_j = None, None
  while len(groups.unique_groups()) > 1:
    _dist, i, j = distances.pop()
    groups.union(i, j)
    last_i, last_j = i, j
  
  sizes = Heap()
  for group in groups.unique_groups():
    group_size = groups.size(group)
    if len(sizes) < 3:
      sizes.push(group_size)
    elif group_size > sizes[0]:
      sizes.push(group_size)
      sizes.pop()
  
  return points[last_i][0] * points[last_j][0]

if __name__ == '__main__':
  run(part1, part2)