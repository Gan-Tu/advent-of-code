import os

# Example Input: 3,4,3,1,2
def parse_input():
  input_filepath = os.path.join(os.path.dirname(__file__), "day6.input")
  numbers = open(input_filepath).read().strip().split(",")
  return [int(x) for x in numbers]

def puzzle1():
  numbers = parse_input()
  for i in range(80):
    new_numbers = []
    create_new = 0
    for n in numbers:
      if n == 0:
        new_numbers.append(6)
        create_new += 1
      else:
        new_numbers.append(n-1)
    for _ in range(create_new):
      new_numbers.append(8)
    numbers = new_numbers
  return len(numbers)



def puzzle2():
  numbers = parse_input()
  # TODO
  return


print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())
