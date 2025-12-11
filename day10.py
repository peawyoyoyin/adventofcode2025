from typing import List, Iterable
from utils.cli import run

def parse_line(line: str):
  tokens = line.strip().split(' ')
  raw_target = tokens[0]
  raw_joltage_requirements = tokens[-1]
  raw_buttons = tokens[1:-1]

  # strip the "[]"
  target = raw_target.strip('[]')
  joltage_requirements = list(map(int, raw_joltage_requirements.strip('{}').split(',')))
  
  buttons = []
  for raw_button in raw_buttons:
    buttons.append(tuple(map(int, raw_button.strip('()').split(','))))

  return (target, buttons, joltage_requirements)

def parse_inputs(inputs: List[str]):
  result = []
  for line in inputs:
    result.append(parse_line(line))
  return result

def transform_lights(state: str, toggles: Iterable[int]):
  next_state = list(state)
  for toggle in toggles:
    next_state[toggle] = '.' if next_state[toggle] == '#' else '#'
  return ''.join(next_state)

def fewest_button_clicks(target: str, buttons: List[Iterable[int]]):
  initial_state = '.'*len(target)
  
  q = [initial_state]
  visited = set([initial_state])
  next_q = []
  rounds = 0

  while q:
    for state in q:
      for button in buttons:
        next_state = transform_lights(state, button)
        if next_state not in visited:
          visited.add(next_state)
          next_q.append(next_state)
    
    rounds += 1

    if any([state == target for state in next_q]):
      break

    q = next_q
    next_q = []
  # assume always found
  return rounds

def part1(inputs: List[str]):
  parsed_inputs = parse_inputs(inputs)

  result = 0
  for target, buttons, joltage_requirements in parsed_inputs:
    result += fewest_button_clicks(target, buttons)
  return result

def transform_counters(counters: Iterable[int], button: Iterable[int]):
  next_state = list(counters)
  for increment in button:
    next_state[increment] += 1
  return tuple(next_state)

def valid_counters(counters: Iterable[int], final_requirements: Iterable[int]):
  assert len(counters) == len(final_requirements)
  return all([counter <= requirement for counter, requirement in zip(counters, final_requirements)])

def fewest_button_clicks2(joltage_requirements: List[int], buttons: List[Iterable[int]]):
  initial_state = tuple(joltage_requirements)
  q = [initial_state]
  next_q = []
  visited = set([initial_state])

  counts = [0] * len(joltage_requirements)
  for button in buttons:
    for toggle in button:
      counts[toggle] += 1
  print(joltage_requirements, counts)
  
  return 0

# TODO not solved
def part2(inputs: List[str]):
  parsed_inputs = parse_inputs(inputs)

  result = 0
  for target, buttons, joltage_requirements in parsed_inputs:
    result += fewest_button_clicks2(joltage_requirements, buttons)
  return result

if __name__ == '__main__':
  run(part1, part2)