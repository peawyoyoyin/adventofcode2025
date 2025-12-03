from argparse import ArgumentParser
from typing import List, Any
from collections.abc import Callable
import time

def load_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  return list(map(lambda l: l.strip(), lines))

def format_ns(ns: int):
  if ns >= 1e9:
    return f'{ns/int(1e9)}s'
  elif ns >= 1e6:
    return f'{ns/int(1e6)}ms'
  elif ns >= 1e3:
    return f'{ns/int(1e3)}us'
  return f'{ns}ns'

def run(part1: Callable[[List[str]], Any], part2: Callable[[List[str]], Any]):
  parser = ArgumentParser()
  parser.add_argument('filename')
  parser.add_argument('-1', '--part1', action='store_true')
  parser.add_argument('-2', '--part2', action='store_true')

  args = parser.parse_args()

  inputs = load_input(args.filename)

  if args.part1 or (not args.part1 and not args.part2):
    start = time.perf_counter_ns()
    part1_sol = part1(inputs)
    end = time.perf_counter_ns()
    print(f'part 1 solution = {part1_sol} ({format_ns(end-start)})')
  
  if args.part2 or (not args.part2 and not args.part2):
    start = time.perf_counter_ns()
    part2_sol = part2(inputs)
    end = time.perf_counter_ns()
    print(f'part 2 solution = {part2_sol} ({format_ns(end-start)})')