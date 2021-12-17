import os
import re
import math

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  pattern = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
  numbers = re.findall(pattern, content.strip())
  assert len(numbers) == 1 and len(numbers[0]) == 4
  return [int(x) for x in numbers[0]]

def sum1toN(n):
  return int(n * (n+1) / 2)

def smallestNtoValue(value):
  i = 1
  while sum1toN(i) < value:
    i += 1
  return i

def puzzle1(data):
  # The idea is that when shooting up, it will eventually goes down to height zero
  # again, and from there, the biggest jump it can take in order to not shot over
  # the area in ONE STEP is abs(y_low), so it should take velocity of abs(y_low) - 1
  # in order to reach back to zero at negative initial velocity.
  # Thus, the highest we can go is 1 + 2+ ... + abs(y_low) - 1
  x_left, x_right, y_low, y_high = data
  return sum1toN(abs(y_low) - 1)

def isValidShot(x_left, x_right, y_low, y_high, initX, initY):
  pos = [0,0]
  vx, vy = initX, initY
  while pos[0] <= x_right and pos[1] >= y_low:
    if pos[0] < x_left and vx == 0:
      return False
    if pos[0] >= x_left and pos[0] <= x_right:
      if pos[1] >= y_low and pos[1] <= y_high:
        return True
    pos[0] += vx
    pos[1] += vy
    vx = max(0, vx-1)
    vy = vy - 1
  return False


def puzzle2(data):
  x_left, x_right, y_low, y_high = data
  # smallest x is when it reaches 0, we just arrived in left
  # highest x is when it reaches right side in one go
  # smallest y is it doesn't shoot over y_low downwards right away
  # highest y is puzzle 1
  result = []
  for x in range(smallestNtoValue(x_left), x_right+1):
    for y in range(y_low, sum1toN(abs(y_low) - 1)+1):
      if isValidShot(x_left, x_right, y_low, y_high, x, y):
        result.append((x,y))
  return len(result)

print("example1: ", puzzle1(parse_input("day17.example")))  # 45
print("puzzle1: ", puzzle1(parse_input("day17.input"))) # 4186
print("example2: ", puzzle2(parse_input("day17.example")))  #  112
print("puzzle2: ", puzzle2(parse_input("day17.input"))) # 2709