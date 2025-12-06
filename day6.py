from typing import List
from utils.cli import run
from utils.assertions import list_assert

from collections import deque
from itertools import batched


def transpose(matrix):
  result = []
  W = len(matrix[0])
  for i in range(W):
    line = []
    for row in matrix:
      line.append(row[i])
    result.append(line)
  return result

def parse_inputs(inputs: List[str]):
  parsed = []
  for line in inputs:
    parsed.append(line.split())
  return transpose(parsed)

def calculate_problem(problem: List[str]):
  operator = problem[-1]

  match operator:
    case '+':
      result = 0
      for token in problem[:-1]:
        result += int(token)
      return result
    case '*':
      result = 1
      for token in problem[:-1]:
        result *= int(token)
      return result
assert calculate_problem(['123', '45', '6', '*']) == 33210
assert calculate_problem(['328', '64', '98', '+']) == 490

def part1(inputs: List[str]):
  problems = parse_inputs(inputs)  
  result = 0
  for problem in problems:
    result += calculate_problem(problem)
  return result

def stream_operator(operators):
  buffer = [operators[0]]
  i = 1
  while i < len(operators):
    while i < len(operators) and operators[i] not in '*+':
      buffer.append(operators[i])
      i += 1
    yield ''.join(buffer)
    if i < len(operators):
      buffer = [operators[i]]
      i += 1
list_assert(list(stream_operator('+   *  ')), ['+   ', '*  '])

def parse_inputs2(inputs: List[str]):
  operands, operators = inputs[:-1], inputs[-1]

  parsed_operators = []
  for parsed_operator in stream_operator(operators):
    parsed_operators.append((parsed_operator.strip(), len(parsed_operator)))

  parsed_operands_1 = []
  for line in operands:
    problem_index = 0
    stream = deque(line)

    parsed_line = []
    for problem_index in range(len(parsed_operators)):
      buffer = []
      for _ in range(parsed_operators[problem_index][1]):
        buffer.append(stream.popleft())
      parsed_line.append(''.join(buffer))
    parsed_operands_1.append(parsed_line)
  parsed_operands_2 = transpose(parsed_operands_1)
  
  parsed = []
  for index, line in enumerate(parsed_operands_2):
    parsed_line = []
    for operand in transpose(line):
      token = ''.join(operand)
      if len(token.strip()) > 0:
        parsed_line.append(token.strip())
    parsed_line.append(parsed_operators[index][0])
    parsed.append(parsed_line)

  return parsed

def part2(inputs: List[str]):
  problems = parse_inputs2(inputs)
  result = 0
  for problem in problems:
    result += calculate_problem(problem)
  return result

if __name__ == '__main__':
  run(part1, part2, False)