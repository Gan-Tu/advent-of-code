import os
from tqdm import tqdm
from heapq import heapify, heappush, heappop, heapreplace

class HeapItem:
  def __init__(self, val, data):
    self.val = val
    self.data = data

  def __eq__(self, other):
    return self.val == other.val and self.data == other.data

  def __lt__(self, other):
    return self.val < other.val

  def __repr__(self):
    return f"{self.val} <- {self.data}"


def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  grid = [[int(x) for x in row] for row in content.split("\n")]
  return grid


def puzzle1(data):
  visited = set()
  dist = {}
  prev = {}
  # initialization
  for r in range(len(data)):
    for c in range(len(data[0])):
      prev[(r,c)] = None
      dist[(r,c)] = float("inf")
  dist[(0,0)] = 0
  visited.add((0,0))

  # queue
  queue = []
  posToHeapItem = {}
  for key, val in dist.items():
    item = HeapItem(val, key)
    posToHeapItem[key] = item
    heappush(queue, item)

  done = False
  end = (len(data)-1, len(data[0])-1)
  with tqdm(total=len(queue)) as pbar:
    while not done and len(queue) > 0:
      x = heappop(queue)
      row, col = x.data
      for dx, dy in [[-1,0], [1,0], [0,1], [0,-1]]:
        row2, col2 = row + dx, col + dy
        if (row2, col2) in dist:
          altDist = dist[(row, col)] + data[row2][col2]
          if altDist < dist[(row2, col2)]:
            dist[(row2, col2)] = altDist
            prev[(row2, col2)] = (row, col)
            q = posToHeapItem[(row2, col2)]
            q.val = altDist
            heapify(queue)
      visited.add((row, col))
      pbar.update(1)
      if (row, col) == end:
        break
  return dist[end]

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("day15.example")))
print("puzzle1: ", puzzle1(parse_input("day15.input")))
# print("example2: ", puzzle2(parse_input("day15.example")))
# print("puzzle2: ", puzzle2(parse_input("day15.input")))
