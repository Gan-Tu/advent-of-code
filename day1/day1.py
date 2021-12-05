def puzzle1():
  numbers = open("day1.input").read()
  numbers = [int(x) for x in numbers.split()]

  count = 0
  for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
      count += 1

  return count


def puzzle2():
  numbers = open("day1.input").read()
  numbers = [int(x) for x in numbers.split()]

  count = 0
  for i in range(3, len(numbers)):
    if numbers[i] > numbers[i-3]:
      count += 1

  return count

print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())