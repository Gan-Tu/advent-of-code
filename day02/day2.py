def puzzle1():
  lines = open("day2.input").read().split("\n")
  forward = 0
  depth = 0
  for line in lines:
    if line.startswith("forward"):
      forward += int(line.replace("forward", "").strip())
    if line.startswith("down"):
      depth += int(line.replace("down", "").strip())
    if line.startswith("up"):
      depth -= int(line.replace("up", "").strip())
  return forward * depth



def puzzle2():
  lines = open("day2.input").read().split("\n")
  forward = 0
  depth = 0
  aim = 0
  for line in lines:
    if line.startswith("down"):
      val = int(line.replace("down", "").strip())
      aim += val
    if line.startswith("up"):
      val = int(line.replace("up", "").strip())
      aim -= val
    if line.startswith("forward"):
      val = int(line.replace("forward", "").strip())
      forward += val
      depth += aim * val
    # print(f"aim: {aim} depth: {depth} forward: {forward}")
  return forward * depth


print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())