import os
import numpy as np
from tqdm import tqdm
import heapdict # pip3 install heapdict

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  grid = [[int(x) for x in row] for row in content.split("\n")]
  return grid

def findShortestDistance(data):
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
  queue = heapdict.heapdict()
  for key, val in dist.items():
    queue[key] = val

  done = False
  end = (len(data)-1, len(data[0])-1)
  with tqdm(total=len(queue)) as pbar:
    while not done and len(queue) > 0:
      (row, col), _ = queue.popitem()
      for dx, dy in [[-1,0], [0,-1], [1,0], [0,1]]:
        row2, col2 = row + dx, col + dy
        if (row2, col2) in dist:
          altDist = dist[(row, col)] + data[row2][col2]
          if altDist < dist[(row2, col2)]:
            dist[(row2, col2)] = altDist
            prev[(row2, col2)] = (row, col)
            queue[(row2, col2)] = altDist
      visited.add((row, col))
      pbar.update(1)
      if (row, col) == end:
        break
  return dist[end]


def puzzle1(data):
  return findShortestDistance(data)

def puzzle2(data):
  data = np.array(data)
  cols = [data]
  for _ in range(4):
    nextData = cols[-1] + 1
    nextData[nextData==10] = 1
    cols.append(nextData)
  cols = np.hstack(cols)
  rows = [cols]
  for _ in range(4):
    nextData = rows[-1] + 1
    nextData[nextData==10] = 1
    rows.append(nextData)
  rows = np.vstack(rows)
  return findShortestDistance(rows)

print("example1: ", puzzle1(parse_input("day15.example")))
print("puzzle1: ", puzzle1(parse_input("day15.input")))
print("example2: ", puzzle2(parse_input("day15.example")))
print("puzzle2: ", puzzle2(parse_input("day15.input")))
