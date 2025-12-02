from typing import List, Tuple
from utils.cli import run
from utils.assertions import list_assert

def parse_range(raw_range: str):
  return tuple(map(int, raw_range.split('-')))

def parse_ranges(raw_input: str):
  return list(map(parse_range, raw_input.split(',')))

def invalid_ids_of_length(start: int, end: int):
  length = len(str(start))
  if length % 2 != 0:
    return
  
  assert len(str(start)) == length
  assert len(str(end)) == length
  
  first_half = int(str(start)[:length//2])
  
  next_invalid_id = int(f'{first_half}{first_half}')
  if next_invalid_id < start:
    first_half += 1
    next_invalid_id = int(f'{first_half}{first_half}')
  while next_invalid_id <= end and len(str(next_invalid_id)) == length:
    yield next_invalid_id
    first_half += 1
    next_invalid_id = int(f'{first_half}{first_half}')
list_assert(list(invalid_ids_of_length(11, 22)), [11, 22])
list_assert(list(invalid_ids_of_length(565653, 565659)), [])
list_assert(list(invalid_ids_of_length(1188511880, 1188511890)), [1188511885])

def split_range_by_length(rnge: Tuple[int, int]):
  start, end = rnge
  if len(str(start)) == len(str(end)):
    yield (start, end)
  else:
    next_start = start
    cur_len = len(str(start))
    while cur_len < len(str(end)):
      yield (next_start, int('9'*cur_len))
      next_start = int('1'+'0'*cur_len)
      cur_len += 1
    yield (next_start, end)
list_assert(list(split_range_by_length((11, 22))), [(11, 22)])
list_assert(list(split_range_by_length((1, 100))), [(1, 9), (10, 99), (100, 100)])

def all_invalid_id_in_range(rnge: Tuple[int, int]):
  for start, end in split_range_by_length(rnge):
    yield from invalid_ids_of_length(start, end)

def part1(inputs: List[str]):
  ranges = parse_ranges(inputs[0])
  ans = 0
  for rnge in ranges:
    ans += sum(all_invalid_id_in_range(rnge))
  return ans

def invalid_ids2_of_length(start: int, end: int):
  """does not guarantee sorted, but still guarantee uniqueness"""  
  length = len(str(start))
  assert len(str(start)) == length
  assert len(str(end)) == length

  visited = set()
  for prefix_len in range(1, (length//2)+1):
    if length % prefix_len == 0:
      prefix = int(str(start)[:prefix_len])
      next_invalid_id = int(str(prefix)*(length//prefix_len))
      while next_invalid_id <= end and len(str(next_invalid_id)) == length:
        if start <= next_invalid_id <= end and next_invalid_id not in visited:
          visited.add(next_invalid_id)
          yield next_invalid_id
        prefix += 1
        next_invalid_id = int(str(prefix)*(length//prefix_len))
list_assert(list(invalid_ids2_of_length(11, 22)),[11, 22])
list_assert(list(invalid_ids2_of_length(565653, 565659)), [565656])
list_assert(list(invalid_ids2_of_length(1188511880, 1188511890)), [1188511885])

def all_invalid_id2_in_range(rnge: Tuple[int, int]):
  for start, end in split_range_by_length(rnge):
    yield from invalid_ids2_of_length(start, end)

def part2(inputs: List[str]):
  ranges = parse_ranges(inputs[0])
  ans = 0
  for rnge in ranges:
    ans += sum(all_invalid_id2_in_range(rnge))
  return ans

if __name__ == '__main__':
  run(part1, part2)