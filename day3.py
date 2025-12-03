from typing import List
from utils.cli import run
from functools import cache

def largest_number_from_bank(bank: str):
  max_so_far = None
  ans = -float('inf')
  for c in bank[::-1]:
    if max_so_far is None:
      max_so_far = int(c)
    else:
      ans = max(ans, int(c)*10+max_so_far)
      max_so_far = max(max_so_far, int(c))
  return ans

assert largest_number_from_bank('987654321111111') == 98

def part1(inputs: List[str]):
  ans = 0
  for bank in inputs:
    ans += largest_number_from_bank(bank)
  return ans

def largest_number_from_bank2(bank: str):
  N = len(bank)
  @cache
  def dp(i, l):
    if l == 1:
      return int(bank[i])
    if i == N-1:
      return int(bank[i])
    suffix = None
    for j in range(i+1, N):
      if suffix is None:
        suffix = dp(j, l-1)
      else:
        suffix = max(suffix, dp(j, l-1))
    return int(bank[i]+str(suffix))
  
  ans = None
  for i in range(N):
    if ans is None:
      ans = dp(i, 12)
    else:
      ans = max(ans, dp(i, 12))
  return int(ans)

assert largest_number_from_bank2('987654321111111') == 987654321111

def part2(inputs: List[str]):
  ans = 0
  for bank in inputs:
    ans += largest_number_from_bank2(bank)
  return ans

if __name__ == '__main__':
  run(part1, part2)