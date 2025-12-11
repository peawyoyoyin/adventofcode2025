from typing import List, Dict, Set, TypeAlias
from utils.cli import run
from collections import defaultdict, deque

Graph: TypeAlias = Dict[str, Set[str]]

def build_graph(inputs: List[str]):
  graph = defaultdict(set)
  for line in inputs:
    st1_tokens = line.strip().split(':')
    key, adj_tokens = st1_tokens[0], st1_tokens[1]
    adjs = adj_tokens.strip().split(' ')
    graph[key].update(adjs)
  return graph

def reverse_graph(graph: Graph):
  result = defaultdict(set)

  for key in graph:
    for adj in graph[key]:
      result[adj].add(key)
  return result

def paths_between_nodes(graph: Graph, src: str, dest: str):
  # first traversal
  st1_graph = defaultdict(set)
  q = deque([src])

  while q:
    top = q.popleft()
    for adj in graph[top]:
      st1_graph[top].add(adj)

      if adj not in st1_graph:
        st1_graph[adj] = set()
        q.append(adj)

  st1_rv = reverse_graph(st1_graph)
  paths = defaultdict(int)
  paths[src] = 1
  q = deque([src])
  while q:
    top = q.popleft()
    for adj in st1_graph[top]:
      paths[adj] += paths[top]
      st1_rv[adj].remove(top)
      if len(st1_rv[adj]) == 0:
        q.append(adj)
    st1_graph.pop(top)
  return paths[dest]

def part1(inputs: List[str]):
  graph = build_graph(inputs)

  return paths_between_nodes(graph, 'you', 'out')  

def part2(inputs: List[str]): 
  graph = build_graph(inputs) 
  case1 = paths_between_nodes(graph, 'svr', 'dac') * paths_between_nodes(graph, 'dac', 'fft') * paths_between_nodes(graph, 'fft', 'out')
  case2 = paths_between_nodes(graph, 'svr', 'fft') * paths_between_nodes(graph, 'fft', 'dac') * paths_between_nodes(graph, 'dac', 'out')
  
  return case1 + case2

if __name__ == '__main__':
  run(part1, part2)