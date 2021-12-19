import os
import ast
import math

DEBUG = False

NODE_ID = 0

class Node:
  def __init__(self, depth, data, parent=None):
    self.parent = parent
    self.isRegularNumber = False
    global NODE_ID
    self.id = NODE_ID
    NODE_ID = NODE_ID+1
    if parent is None:
      assert depth == 0
    if type(data) == list:
      assert len(data) == 2
      self.depth = depth
      self.left = Node(depth+1, data[0], self)
      self.right = Node(depth+1, data[1], self)
    else:
      self.isRegularNumber = True
      self.value = data
      self.depth = depth - 1

  @property
  def isRegularPair(self):
    if self.isRegularNumber:
      return False
    return self.left.isRegularNumber and self.right.isRegularNumber

  @property
  def data(self):
    if self.isRegularNumber:
      return self.value
    else:
      return [self.left.data, self.right.data]

  def addValue(self, val):
    assert self.isRegularNumber
    self.value += val

  def __repr__(self):
    if self.isRegularNumber:
      if DEBUG:
        # return f"RegularNumber(data={self.data},depth={self.depth})"
        return f"({self.data}, depth={self.depth})"
      else:
        return str(self.data)
    else:
      return f"[{self.left}, {self.right}]"

  @property
  def magnitude(self):
    if self.isRegularNumber:
      return self.data
    return 3 * self.left.magnitude + 2 * self.right.magnitude

  def addToLeftMostRegularNumber(self, val):
    if self.isRegularNumber:
      self.addValue(val)
      return True
    if self.left.addToLeftMostRegularNumber(val):
      return True
    if self.right.addToLeftMostRegularNumber(val):
      return True
    return False

  def addToRightMostRegularNumber(self, val):
    if self.isRegularNumber:
      self.addValue(val)
      return True
    if self.right.addToRightMostRegularNumber(val):
      return True
    if self.left.addToRightMostRegularNumber(val):
      return True
    return False

  def __add__(self, other):
    return Node(0, [self.data, other.data])

  def __eq__(self, other):
    return self.data == other

  def split(self):
    if self.isRegularNumber:
      if self.data >= 10:
        values = [math.floor(self.data/2), math.ceil(self.data/2)]
        self.__init__(self.depth+1, values, self.parent)
        return True
    else:
      if self.left.split() or self.right.split():
        return True
    return False

  def explode(self):
    if self.isRegularNumber:
      return False
    if self.left.explode() or self.right.explode():
      return True
    if self.depth >= 4:
      assert self.left.isRegularNumber
      assert self.right.isRegularNumber
      leftVal, rightVal = self.left.data, self.right.data
      self.__init__(self.depth, 0, self.parent)
      # add left values
      cur = self.parent
      exclude = [self.id]
      while cur is not None:
        if cur.left.id not in exclude:
          if cur.left.addToRightMostRegularNumber(leftVal):
            break
        exclude.append(cur.id)
        cur = cur.parent
      # add right values
      cur = self.parent
      exclude = [self.id]
      while cur is not None:
        if cur.right.id not in exclude:
          if cur.right.addToLeftMostRegularNumber(rightVal):
            break
        exclude.append(cur.id)
        cur = cur.parent
      return True
    return False

def parse_test_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  content = content.split("\n")
  content = [x.split(" -> ") for x in content]
  content = [[ast.literal_eval(x) for x in pair] for pair in content]
  return content

def test_explode():
  data = parse_test_input("explode.example")
  passed = True
  for inp, expected in data:
    node = Node(0, inp)
    assert node.explode()
    actual = node.data
    if actual != expected:
      passed = False
      print(f"Input: {inp};\nExpected: {expected}; Actual: {actual}")
  if passed:
    print("Passed")

def test_magnitude():
  data = parse_test_input("magnitude.example")
  passed = True
  for inp, expected in data:
    node = Node(0, inp)
    actual = node.magnitude
    if actual != expected:
      passed = False
      print(f"Input: {inp};\nExpected: {expected}; Actual: {actual}")
  if passed:
    print("Passed")

def test_split():
  data = parse_test_input("split.example")
  passed = True
  for inp, expected in data:
    node = Node(0, inp)
    assert node.split()
    actual = node.data
    if actual != expected:
      passed = False
      print(f"Input: {inp};\nExpected: {expected}; Actual: {actual}")
  if passed:
    print("Passed")


print("\n\n============ Testing explode ============")
test_explode()

print("\n\n============ Testing magnitude ============")
test_magnitude()

print("\n\n============ Testing split ============")
test_split()


def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  content = content.split("\n")
  content = [ast.literal_eval(seq) for seq in content]
  content = [Node(0, x) for x in content]
  return content

def runReduce(data):
  while True:
    if data.explode():
      continue
    if data.split():
      continue
    break
  return data

def puzzle1(data):
  result = None
  for n in data:
    if result is None:
      result = n
    else:
      result += n
    runReduce(result)
  # print(result)
  return result.magnitude


def puzzle2(data):
  largest = -1
  largestPair = []
  for i in range(len(data)):
    for j in range(0, len(data)):
      if i == j: continue
      node = data[i] + data[j]
      runReduce(node)
      if node.magnitude > largest:
        largestPair = [data[i], data[j]]
        largest = node.magnitude
  # print(largestPair)
  return largest


print("\n\n======= Examples & Puzzles =============")
print("example 1.0: ", puzzle1(parse_input("day18.example0")))
print("example 1.1: ", puzzle1(parse_input("day18.example1")))
print("example 1.2: ", puzzle1(parse_input("day18.example2")))
print("example 1.3: ", puzzle1(parse_input("day18.example3")))
print("example 1.4: ", puzzle1(parse_input("day18.example4")))
print("example 1.5: ", puzzle1(parse_input("day18.example5")))

print("puzzle1: ", puzzle1(parse_input("day18.input")))

print("example 2", puzzle2(parse_input("day18.example5")))
print("puzzle2: ", puzzle2(parse_input("day18.input")))
