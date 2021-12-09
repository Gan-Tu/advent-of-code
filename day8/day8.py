import os

DIGIT_TO_SEGMENT_COUNT = {
  0: 6,
  1: 2, # unique
  2: 5,
  3: 5,
  4: 4, # unique
  5: 5,
  6: 6,
  7: 3, # unique
  8: 7, # unique
  9: 6,
}


def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  lines = content.split("\n")
  result = []
  for line in lines:
    left, right = line.split("|")
    left = left.strip().split()
    right = right.strip().split()
    result.append([left, right])
  return result

def puzzle1(data):
  total = 0
  for left, right in data:
    total += len([x for x in right if len(x) in [2,4,3,7]])
  return total

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("day8.example")))
print("puzzle1: ", puzzle1(parse_input("day8.input")))
# print("example2: ", puzzle2(parse_input("day8.example")))
# print("puzzle2: ", puzzle2(parse_input("day8.input")))
