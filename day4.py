from typing import List, Tuple
from utils.cli import run
from collections import deque, defaultdict

def create_grid(inputs: List[str]):
  return list(map(list, inputs))

def adjacent_coords(coord: Tuple[int, int], size: Tuple[int, int]):
  """
  coord: (row, col)
  size: (rows, cols)
  """
  r, c = coord
  rs, cs = size
  for dr in (-1, 0, 1):
    for dc in (-1, 0, 1):
      if (dr, dc) == (0, 0):
        continue

      if 0 <= r+dr < rs and 0 <= c+dc < cs:
        yield (r+dr, c+dc)

def part1(inputs: List[str]):
  grid = create_grid(inputs)
  rows, cols = len(grid), len(grid[0])

  ans = 0
  for row in range(rows):
    for col in range(cols):
      adj_rolls = 0
      for adj_row, adj_col in adjacent_coords((row, col), (rows, cols)):
        if grid[adj_row][adj_col] == '@':
          adj_rolls += 1
      if grid[row][col] == '@' and adj_rolls < 4:
        ans += 1
  return ans

def part2(inputs: List[str]):
  grid = create_grid(inputs)
  rows, cols = len(grid), len(grid[0])

  q = deque()
  adj_roll_counts = defaultdict(int)

  visited = set()
  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == '@':
        adj_rolls = 0
        for adj_row, adj_col in adjacent_coords((row, col), (rows, cols)):
          if grid[adj_row][adj_col] == '@':
            adj_rolls += 1
        adj_roll_counts[(row, col)] = adj_rolls
        if adj_rolls < 4:
          q.append((row, col))
          visited.add((row, col))

  ans = 0
  while len(q) > 0:
    row, col = q.popleft()
    grid[row][col] = 'x'
    ans += 1
    for adj_row, adj_col in adjacent_coords((row, col), (rows, cols)):
      if grid[adj_row][adj_col] == '@' and (adj_row, adj_col) in adj_roll_counts:
        adj_roll_counts[(adj_row, adj_col)] -= 1
        if (adj_row, adj_col) not in visited and adj_roll_counts[(adj_row, adj_col)] < 4:
          q.append((adj_row, adj_col))
          visited.add((adj_row, adj_col))
  return ans

if __name__ == '__main__':
  run(part1, part2)