from typing import List
from utils.cli import run

def parse_instruction(inst: str):
  return inst[0], int(inst[1:])

def rotate(dial: int, instruction: str) -> int:
  direction, magnitude = parse_instruction(instruction)

  match direction:
    case 'R': # up
      dial += magnitude
    case 'L': # down
      dial -= magnitude
      if dial < 0:
        dial = 100 - (abs(dial) % 100)
  dial %= 100
  return dial

assert rotate(0, 'R1') == 1
assert rotate(0, 'R100') == 0
assert rotate(0, 'L1') == 99
assert rotate(0, 'R201') == 1
assert rotate(0, 'L99') == 1
assert rotate(0, 'L20') == 80
assert rotate(99, 'R1') == 0
assert rotate(50, 'L150') == 0

def part1(inputs: List[str]):
  dial = 50
  ans = 0
  
  for inst in inputs:
    dial = rotate(dial, inst)
    if dial == 0:
      ans += 1
  return ans

def part2(inputs: List[str]):
  dial = 50
  ans = 0

  for inst in inputs:
    direction, magnitude = parse_instruction(inst)

    revolutions = magnitude // 100
    ans += revolutions

    real_mag = magnitude % 100
    match direction:
      case 'R': # up
        if real_mag + dial > 100:
          ans += 1
        dial = (real_mag + dial) % 100
      case 'L': # down
        if real_mag > dial and dial > 0:
          ans += 1
        dial -= real_mag
        if dial < 0:
          dial = 100 - (abs(dial) % 100)
    dial %= 100
    if dial == 0 and real_mag > 0:
      ans += 1
  return ans

if __name__ == '__main__':
  run(part1, part2)