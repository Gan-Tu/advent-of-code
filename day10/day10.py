import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  return content.split("\n")

SCORE_TABLE = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

def isOpen(x):
  return x in "([{<"

def isClose(x):
  return x in ")]}>"

def isClosingPair(x, y):
  if x == "(": return y == ")"
  if x == "[": return y == "]"
  if x == "{": return y == "}"
  if x == "<": return y == ">"
  return False

def puzzle1(data, verbose=False):
  badCharacters = list()
  for line in data:
    queue = list()
    hasBad = False
    if verbose: print(line)
    for c in line:
      if verbose: print(queue, f"c = {c}")
      if isOpen(c):
        queue.append(c)
      elif isClose(c):
        if len(queue) == 0:
          badCharacters.append(c)
          hasBad = True
          break
        lastC = queue.pop()
        if not isClosingPair(lastC, c):
          badCharacters.append(c)
          hasBad = True
          break
  score = 0
  for c in SCORE_TABLE:
    score += SCORE_TABLE[c] * badCharacters.count(c)
  return score

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("day10.example")))
print("puzzle1: ", puzzle1(parse_input("day10.input")))
# print("example2: ", puzzle2(parse_input("day10.example")))
# print("puzzle2: ", puzzle2(parse_input("day10.input")))
