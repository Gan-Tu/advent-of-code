import os

# Example Input: 16,1,2,0,4,2,7,1,2,14
def parse_input():
  input_filepath = os.path.join(os.path.dirname(__file__), "day7.input")
  numbers = open(input_filepath).read().strip().split(",")
  return [int(x) for x in numbers]

def puzzle1():
  numbers = parse_input()
  smallest = float("inf")
  for i in range(min(numbers), max(numbers)+1):
    val = sum([abs(x-i) for x in numbers])
    smallest = min(smallest, val)
  return smallest


def puzzle2():
  lines = parse_input()
  # TODO
  return


print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())
