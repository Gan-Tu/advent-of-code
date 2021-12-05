def parse_board(board_str):
  result = []
  for row in board_str.strip().split("\n"):
    result.append([])
    for col in row.strip().split():
      result[-1].append(int(col))
  return result

def parse_input():
  sections = open("day4.input").read().split("\n\n")
  inputs = [int(x) for x in sections[0].strip().split(",")]
  boards = []
  for board_str in sections[1:]:
    boards.append(parse_board(board_str))
  return inputs, boards

def mark_board(board, value):
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] == value:
        board[r][c] = True
  return board

def check_board(board):
  for row in board:
    if all([x == True for x in row]):
      return True
  for i in range(len(board[0])):
    col = [row[i] for row in board]
    if all([x == True for x in col]):
      return True
  return False

def sum_unmarked(board):
  result = 0
  for row in board:
    for val in row:
      if val != True:
        result += val
  return result

def puzzle1():
  inputs, boards = parse_input()
  for n in inputs:
    boards = [mark_board(b, n) for b in boards]
    for b in boards:
      if check_board(b):
        return sum_unmarked(b) * n

def puzzle2():
  inputs, boards = parse_input()
  for n in inputs:
    boards = [mark_board(b, n) for b in boards]
    not_won_boards = [b for b in boards if not check_board(b)]
    if len(not_won_boards) == 0:
      b = boards[-1]
      return sum_unmarked(b) * n
    boards = not_won_boards

print("puzzle1", puzzle1())
print("puzzle2", puzzle2())