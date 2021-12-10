import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  rows = content.split("\n")
  data = [[int(x) for x in row] for row in rows]
  return data

def puzzle1(data):
  total = 0
  for r in range(len(data)):
    for c in range(len(data[r])):
      isLowPoint = True
      for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        r2, c2 = r + dr, c + dc
        if r2 >= 0 and r2 < len(data):
          if c2 >= 0 and c2 < len(data[r]):
            if data[r2][c2] <= data[r][c]:
              isLowPoint = False
      if isLowPoint:
        total += data[r][c] + 1
  return total

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("day9.example")))
print("puzzle1: ", puzzle1(parse_input("day9.input")))
# print("example2: ", puzzle2(parse_input("day9.example")))
# print("puzzle2: ", puzzle2(parse_input("day9.input")))
