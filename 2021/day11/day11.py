import os
import numpy as np

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  content = content.split("\n")
  content = [[int(x) for x in row] for row in content]
  return np.array(content)

def display(grid, flash='0'):
  rows = ["".join([str(x) if x <= 9 and x > 0 else flash for x in row]) for row in grid]
  rows = "\n".join(rows)
  return f"\n{rows}\n"

def safe_incr(data, i, j):
  if i >= 0 and j >= 0:
    if i < len(data) and j < len(data[0]):
      data[i][j] += 1

def flash_neighbors(data):
  flashedData = set()
  while True:
    flashed = False
    for i in range(len(data)):
      for j in range(len(data[0])):
        if data[i][j] > 9 and (i,j) not in flashedData:
          flashedData.add((i,j))
          safe_incr(data, i-1, j-1)
          safe_incr(data, i-1, j)
          safe_incr(data, i-1, j+1)
          safe_incr(data, i, j-1)
          safe_incr(data, i, j+1)
          safe_incr(data, i+1, j-1)
          safe_incr(data, i+1, j)
          safe_incr(data, i+1, j+1)
          flashed = True
    if not flashed:
      break
  return len(flashedData)

def puzzle1(data, verbose=False):
  if verbose:
    print(f"day 0 {display(data)}")
  total = 0
  for day in range(100):
    data = data + 1
    total += flash_neighbors(data)
    data = data.clip(0,10) % 10
    if verbose:
      print(f"day {day+1} {display(data)}")
  return total

def puzzle2(data, verbose=False):
  day = 1
  while True:
    data = data + 1
    total = flash_neighbors(data)
    data = data.clip(0,10) % 10
    if total == (len(data) * len(data[0])):
      return day
    day += 1

print("example1: ", puzzle1(parse_input("day11.example")))
print("puzzle1: ", puzzle1(parse_input("day11.input")))
print("example2: ", puzzle2(parse_input("day11.example")))
print("puzzle2: ", puzzle2(parse_input("day11.input")))
