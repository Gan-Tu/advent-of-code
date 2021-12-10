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
  basinSizes = []
  visited = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
  for r in range(len(data)):
    for c in range(len(data[r])):
      if data[r][c] == 9:
        visited[r][c] = True
        continue
      if visited[r][c]:
        continue
      # bread first search fan out
      queue = [(r,c)]
      size = 1
      visited[r][c] = True
      while len(queue) > 0:
        y,x = queue.pop(0)
        # print(basinSizes, size, (y,x))
        for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]:
          y2, x2 = y + dy, x + dx
          if y2 >= 0 and y2 < len(data):
            if x2 >= 0 and x2 < len(data[r]):
              if data[y2][x2] == 9:
                visited[y2][x2] = True
                continue
              if visited[y2][x2]:
                continue
              size += 1
              queue.append((y2, x2))
              visited[y2][x2] = True
      basinSizes.append(size)
  basinSizes = sorted(basinSizes, reverse=True)
  return basinSizes[0] * basinSizes[1] * basinSizes[2]

print("example1: ", puzzle1(parse_input("day9.example")))
print("puzzle1: ", puzzle1(parse_input("day9.input")))
print("example2: ", puzzle2(parse_input("day9.example")))
print("puzzle2: ", puzzle2(parse_input("day9.input")))
