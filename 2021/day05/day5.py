def parse_input():
  result = []
  height = 0
  width = 0
  for line in open("day5.input").read().split("\n"):
    sides = line.split(" -> ")
    assert len(sides) == 2
    start = [int(x) for x in sides[0].strip().split(",")]
    end = [int(x) for x in sides[1].strip().split(",")]
    assert len(start) == 2 and len(end) == 2
    result.append([start, end])
    height = max(height, max(start[0], end[0]))
    width = max(width, max(start[1], end[1]))
  return result, height + 1, width  + 1

def puzzle1():
  lines, height, width = parse_input()
  board = [[0 for _ in range(width)] for _ in range(height)]
  for start, end in lines:
    if start[0] == end[0]:
      for i in range(min(start[1], end[1]), max(start[1], end[1])+1):
        board[i][start[0]] += 1
    if start[1] == end[1]:
      for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
        board[start[1]][i] += 1
  result = 0
  for row in board:
    for c in row:
      if c > 1:
        result += 1
  return result

def show(start, end, board):
  print(start, end)
  print('\n'.join([''.join([str(x) for x in row]) for row in board]).replace('0','.'))
  print()

def puzzle2():
  lines, height, width = parse_input()
  board = [[0 for _ in range(width)] for _ in range(height)]
  for start, end in lines:
    if start[0] == end[0]:
      for i in range(min(start[1], end[1]), max(start[1], end[1])+1):
        board[i][start[0]] += 1
      # show(start, end, board)
      continue
    if start[1] == end[1]:
      for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
        board[start[1]][i] += 1
      # show(start, end, board)
      continue
    x, y = start[0], start[1]
    while x != end[0] and y != end[1]:
      board[y][x] += 1
      x += 1 if x < end[0] else -1
      y += 1 if y < end[1] else -1
    board[y][x] += 1
    # show(start, end, board)
  result = 0
  for row in board:
    # print(row)
    for c in row:
      if c > 1:
        result += 1
  return result


print("puzzle1", puzzle1())
print("puzzle2", puzzle2())
