import os

# Example Input: 3,4,3,1,2
def parse_input():
  input_filepath = os.path.join(os.path.dirname(__file__), "day6.input")
  numbers = open(input_filepath).read().strip().split(",")
  return [int(x) for x in numbers]

def breedCount(timers, daysElapsed):
  counts = [timers.count(i) for i in range(9)]
  for _ in range(daysElapsed):
    cnt = counts.pop(0)
    counts.append(cnt)
    counts[6] += cnt
  return sum(counts)

def puzzle1(verbose=False):
  numbers = parse_input()
  return breedCount(numbers, 80)

def puzzle2():
  numbers = parse_input()
  return breedCount(numbers, 256)

print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())
