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

def puzzle1(data):
  # The idea is that when shooting up, it will eventually goes down to height zero
  # again, and from there, the biggest jump it can take in order to not shot over
  # the area in ONE STEP is abs(y_low), so it should take velocity of abs(y_low) - 1
  # in order to reach back to zero at negative initial velocity.
  # Thus, the highest we can go is 1 + 2+ ... + abs(y_low) - 1
  x_left, x_right, y_low, y_high = data
  return sum1toN(abs(y_low) - 1)

def puzzle2(data):
  # TODO
  return data

print("example1: ", puzzle1(parse_input("day17.example")))
print("puzzle1: ", puzzle1(parse_input("day17.input")))
# print("example2: ", puzzle2(parse_input("day17.example")))
# print("puzzle2: ", puzzle2(parse_input("day17.input")))


