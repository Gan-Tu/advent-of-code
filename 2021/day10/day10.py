import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  return content.split("\n")

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

def getClosingPair(x):
  if x == "(": return ")"
  if x == "[": return "]"
  if x == "{": return "}"
  if x == "<": return ">"
  raise RuntimeError(f"not valid open {x}")

def puzzle1(data, verbose=False):
  badCharacters = list()
  for line in data:
    queue = list()
    if verbose: print(line)
    for c in line:
      if verbose: print(queue, f"c = {c}")
      if isOpen(c):
        queue.append(c)
      elif isClose(c):
        if len(queue) == 0:
          badCharacters.append(c)
          break
        lastC = queue.pop()
        if not isClosingPair(lastC, c):
          badCharacters.append(c)
          break
  score = 0
  SCORE_TABLE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
  }
  for c in SCORE_TABLE:
    score += SCORE_TABLE[c] * badCharacters.count(c)
  return score

def puzzle2(data, verbose=False):
  completions = list()
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
          hasBad = True
          break
        lastC = queue.pop()
        if not isClosingPair(lastC, c):
          hasBad = True
          break
    if not hasBad:
      if len(queue) != 0:
        missing = []
        while len(queue) > 0:
          missing.append(getClosingPair(queue.pop()))
        completions.append("".join(missing))

  scores = []
  SCORE_TABLE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
  }
  for seq in completions:
    total = 0
    for c in seq:
      total = total * 5 + SCORE_TABLE[c]
    scores.append(total)
  scores = sorted(scores)
  return scores[len(scores)//2]

print("example1: ", puzzle1(parse_input("day10.example")))
print("puzzle1: ", puzzle1(parse_input("day10.input")))
print("example2: ", puzzle2(parse_input("day10.example")))
print("puzzle2: ", puzzle2(parse_input("day10.input")))
