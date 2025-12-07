from typing import List
from utils.cli import run

from collections import deque
from functools import cache

def part1(inputs: List[str]):
  start = inputs[0].index('S')
  W, H = len(inputs[0]), len(inputs)

  visited = set((0, start))
  q = deque([(0, start)])
  splits = 0

  while q:
    (row, col) = q.popleft()
    
    if 0 <= row < H and 0 <= col < W:
      match inputs[row][col]:
        case '.' | 'S':
          if (row+1, col) not in visited and 0 <= row+1 < H:
            visited.add((row+1, col))
            q.append((row+1, col))
        case '^':
          splits += 1
          if (row, col-1) not in visited and 0 <= col-1 < W:
            visited.add((row, col-1))
            q.append((row, col-1))
          if (row, col+1) not in visited and 0 <= col+1 < W:
            visited.add((row, col+1))
            q.append((row, col+1))

  return splits

def part2(inputs: List[str]):
  @cache
  def count_paths(row, col):
    if row == len(inputs)-1:
      return 1
    if col < 0 or col >= len(inputs[0]):
      return 0
    
    match inputs[row][col]:
      case '.' | 'S':
        return count_paths(row+1, col)
      case '^':
        return count_paths(row, col-1) + count_paths(row, col+1)
  start = inputs[0].index('S')
  return count_paths(0, start)

if __name__ == '__main__':
  run(part1, part2)