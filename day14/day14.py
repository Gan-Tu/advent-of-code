import os
from collections import Counter

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  seq, mappings = content.split("\n\n")
  seq = seq.strip()
  mappings = [x.split(" -> ") for x in mappings.split("\n")]
  return seq, dict(mappings)

# def puzzle1(data):
#   seq, mappings = data
#   print(seq)
#   for day in range(4):
#     for key, value in mappings.items():
#       seq = seq.replace(key, f"{key[0]}{value.lower()}{key[1]}")
#     print(seq)
#     seq = seq.upper()
#     print(f"day {day+1}: {seq}")
#   counts = Counter(seq)
#   print(counts)
#   values = counts.values()
#   return max(values) - min(values)

def puzzle1(data):
  seq, mappings = data
  # print(seq)
  for day in range(10):
    result = []
    for i in range(len(seq)-1):
      result.append(seq[i])
      if seq[i:i+2] in mappings:
        result.append(mappings[seq[i:i+2]])
    result.append(seq[-1])
    seq = "".join(result)
    # print(seq)
  counts = Counter(seq)
  # print(counts)
  values = counts.values()
  return max(values) - min(values)

def puzzle2(data):
  seq, mappings = data
  counts = { x: 0 for x in mappings}
  for i in range(len(seq)-1):
    s = seq[i:i+2]
    if s in counts:
      counts[s] += 1
  result = Counter(seq)
  for _ in range(40):
    for key, val in list(counts.items()):
      if val > 0:
        s1 = key[0] + mappings[key]
        s2 = mappings[key] + key[1]
        if s1 in counts:
          counts[s1] += val
        if s2 in counts:
          counts[s2] += val
        result[mappings[key]] += val
        counts[key] -= val
  vals = result.values()
  return max(vals) - min(vals)

print("example1: ", puzzle1(parse_input("day14.example")))
print("puzzle1: ", puzzle1(parse_input("day14.input")))
print("example2: ", puzzle2(parse_input("day14.example")))
print("puzzle2: ", puzzle2(parse_input("day14.input")))
