from typing import List, Tuple
from utils.cli import run
from collections import deque

def parse_range(line: str):
  parsed = tuple(map(int, line.strip().split('-')))
  assert len(parsed) == 2, f'invalid range ${parsed}'
  return parsed

def parse_inputs(inputs: List[str]):
  stream = deque(inputs)
  ranges = []
  
  while True:
    next_line = stream.popleft()
    if next_line == '':
      break
    ranges.append(parse_range(next_line))
  
  ids = list(map(int, stream))
  return (ranges, ids)

def range_overlap(range1, range2):
  """assumes range1 < range2"""
  start1, end1 = range1
  start2, end2 = range2
  assert start1 <= start2, f'range1 is not before range2, {range1}, {range2}'
  return start1 <= start2 <= end1

def merge_range(range1, range2):
  start1, end1 = range1
  start2, end2 = range2
  return (min(start1, start2), max(end1, end2))

# sort and merge overlapping ranges
def sort_merge_ranges(ranges: List[str]):
  new_ranges = []

  cur_range = None
  for rnge in sorted(ranges):
    if cur_range is None:
      cur_range = rnge
    elif range_overlap(cur_range, rnge):
      cur_range = merge_range(cur_range, rnge)
    else:
      new_ranges.append(cur_range)
      cur_range = rnge
  # last one
  new_ranges.append(cur_range)
  return new_ranges

def find_range(iid: int, ranges: List[Tuple[int, int]]):
  l, r = 0, len(ranges)-1
  
  while l <= r:
    mid = (l+r) // 2
    
    (start, end) = ranges[mid]

    if start <= iid <= end:
      return mid
    elif iid < start:
      r = mid-1
    else:
      l = mid+1
  return None

def part1(inputs: List[str]):
  (ranges, iids) = parse_inputs(inputs)
  ranges = sort_merge_ranges(ranges)

  fresh = 0
  for iid in iids:
    if find_range(iid, ranges) is not None:
      fresh += 1
  return fresh

def part2(inputs: List[str]):
  (ranges, iids) = parse_inputs(inputs)
  ranges = sort_merge_ranges(ranges)

  total = 0
  for start, end in ranges:
    total += end - start +1
  return total

if __name__ == '__main__':
  run(part1, part2)