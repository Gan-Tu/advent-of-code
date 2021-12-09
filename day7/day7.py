import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  return [int(x) for x in content.strip().split(",")]

def puzzle1(data):
  smallest = float("inf")
  for i in range(min(data), max(data)+1):
    val = sum([abs(x-i) for x in data])
    smallest = min(smallest, val)
  return smallest

def puzzle2(data):
  smallest = float("inf")
  fuelCost = lambda n: n*(n+1)/2
  for i in range(min(data), max(data)+1):
    val = int(sum([fuelCost(abs(x-i)) for x in data]))
    smallest = min(smallest, val)
  return smallest



print("example1: ", puzzle1(parse_input("day7.example")))
print("puzzle1: ", puzzle1(parse_input("day7.input")))
print("example2: ", puzzle2(parse_input("day7.example")))
print("puzzle2: ", puzzle2(parse_input("day7.input")))
