from argparse import ArgumentParser
from typing import List, Any
from collections.abc import Callable

def load_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  return list(map(lambda l: l.strip(), lines))

def run(part1: Callable[[List[str]], Any], part2: Callable[[List[str]], Any]):
  parser = ArgumentParser()
  parser.add_argument('filename')
  parser.add_argument('-1', '--part1', action='store_true')
  parser.add_argument('-2', '--part2', action='store_true')

  args = parser.parse_args()

  inputs = load_input(args.filename)

  if args.part1 or (not args.part1 and not args.part2):
    part1_sol = part1(inputs)
    print(f'part 1 solution = {part1_sol}')
  
  if args.part2 or (not args.part2 and not args.part2):
    part2_sol = part2(inputs)
    print(f'part 2 solution = {part2_sol}')