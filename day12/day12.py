import os

class Graph:
  def __init__(self):
    self.neighbors = dict()

  def add_edge(self, x, y):
    if x not in self.neighbors:
      self.neighbors[x] = set()
    self.neighbors[x].add(y)
    if y not in self.neighbors:
      self.neighbors[y] = set()
    self.neighbors[y].add(x)

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  edges = content.split("\n")
  g = Graph()
  for e in edges:
    left, right = e.split("-")
    g.add_edge(left, right)
  return g


# TODO: add memoization
def countPaths(graph, cur, curVisited):
  if cur not in graph.neighbors:
    return 0
  if cur in curVisited and not cur.isupper():
    return 0
  if cur == "end":
    return 1
  total = 0
  curVisited.add(cur)
  for v in graph.neighbors[cur]:
    total += countPaths(graph, v, curVisited.copy())
  return total


def puzzle1(graph):
  if "start" not in graph.neighbors and "end" not in graph.neighbors:
    return 0
  return countPaths(graph, "start", set())

def puzzle2(data):
  # TODO
  return

print("example 1.1: ", puzzle1(parse_input("day12.example1")))
print("example 1.2: ", puzzle1(parse_input("day12.example2")))
print("example 1.3: ", puzzle1(parse_input("day12.example3")))
print("puzzle1: ", puzzle1(parse_input("day12.input")))

# print("example 2.1: ", puzzle2(parse_input("day12.example1")))
# print("example 2.2: ", puzzle2(parse_input("day12.example2")))
# print("example 2.3: ", puzzle2(parse_input("day12.example3")))
# print("puzzle2: ", puzzle2(parse_input("day12.input")))
