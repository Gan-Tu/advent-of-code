import os

DIGIT_TO_SEGMENT_COUNT = {
  0: 6,
  6: 6,
  9: 6,

  1: 2, # unique
  4: 4, # unique
  7: 3, # unique
  8: 7, # unique

  2: 5,
  3: 5,
  5: 5,
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

def build_mapping(one, four, seven, eight, data):
  result = {
    "TOP": None,
    "RIGHT_UP": None,
    "RIGHT_BOTTOM": None,
    "MIDDLE": None,
    "BOTTOM": None,
    "LEFT_UP": None,
    "LEFT_BOTTOM": None,
  }
  one = set(one)
  four = set(four)
  seven = set(seven)
  eight = set(eight)
  # early deductions
  TOP = seven.difference(one) # unique
  assert len(TOP) == 1
  result["TOP"] = list(TOP)[0]
  # same below
  RIGHT_UP = one
  RIGHT_BOTTOM = one
  assert RIGHT_UP == RIGHT_BOTTOM
  # same below
  MIDDLE = four.difference(one)
  LEFT_UP = four.difference(one).intersection(eight.difference(seven))
  assert MIDDLE == LEFT_UP
  # same below
  BOTTOM = eight.difference(four).intersection(eight.difference(seven))
  LEFT_BOTTOM = eight.difference(four).difference(TOP)
  assert BOTTOM == LEFT_BOTTOM
  # further eliminations
  zero_six_nine = [x for x in data if len(x) == 6]
  two_three_five = [x for x in data if len(x) == 5]
  # only right up is not in all of zero, six, nine
  for x in RIGHT_UP:
    for w in zero_six_nine:
      if x not in w:
        result["RIGHT_UP"] = x
        break
  if result["RIGHT_UP"] is not None:
    RIGHT_BOTTOM = RIGHT_BOTTOM.difference(result["RIGHT_UP"])
    assert len(RIGHT_BOTTOM) == 1
    result["RIGHT_BOTTOM"] = list(RIGHT_BOTTOM)[0]
  # only middle up is not in all of zero, six, nine
  for x in MIDDLE:
    for w in zero_six_nine:
      if x not in w:
        result["MIDDLE"] = x
        break
  if result["MIDDLE"] is not None:
    LEFT_UP = LEFT_UP.difference(result["MIDDLE"])
    assert len(LEFT_UP) == 1
    result["LEFT_UP"] = list(LEFT_UP)[0]
  # only left bottom is not in all of zero, six, nine
  for x in LEFT_BOTTOM:
    for w in zero_six_nine:
      if x not in w:
        result["LEFT_BOTTOM"] = x
        break
  if result["LEFT_BOTTOM"] is not None:
    BOTTOM = BOTTOM.difference(result["LEFT_BOTTOM"])
    assert len(BOTTOM) == 1
    result["BOTTOM"] = list(BOTTOM)[0]
  return result

def get_number(sequence, mapping):
  if len(sequence) == 2: return 1
  if len(sequence) == 4: return 4
  if len(sequence) == 3: return 7
  if len(sequence) == 7: return 8
  if len(sequence) == 6:
    if mapping["MIDDLE"] not in sequence:
      return 0
    if mapping["RIGHT_UP"] not in sequence:
      return 6
    if mapping["LEFT_BOTTOM"] not in sequence:
      return 9
    raise RuntimeError(f"Unexpected sequence: {sequence}; mappings: {mapping}")
  if len(sequence) == 5:
    if mapping["LEFT_UP"] in sequence:
      return 5
    if mapping["LEFT_BOTTOM"] in sequence:
      return 2
    if mapping["BOTTOM"] in sequence:
      return 3
    raise RuntimeError(f"Unexpected sequence: {sequence}; mappings: {mapping}")
  raise RuntimeError(f"Unexpected sequence: {sequence}; mappings: {mapping}")


def puzzle1(data):
  total = 0
  for left, right in data:
    total += len([x for x in right if len(x) in [2,4,3,7]])
  return total

def puzzle2(data):
  total = 0
  for left, right in data:
    one = [x for x in left if len(x) == 2][0]
    four = [x for x in left if len(x) == 4][0]
    seven = [x for x in left if len(x) == 3][0]
    eight = [x for x in left if len(x) == 7][0]
    mappings = build_mapping(one, four, seven, eight, left)
    output = [get_number(x, mappings) for x in right]
    total += output[0] * 1000 + output[1] * 100 + output[2] * 10 + output[3]
  return total

print("example1: ", puzzle1(parse_input("day8.example")))
print("puzzle1: ", puzzle1(parse_input("day8.input")))
print("example2: ", puzzle2(parse_input("day8.example")))
print("puzzle2: ", puzzle2(parse_input("day8.input")))

