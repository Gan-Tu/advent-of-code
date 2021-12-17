def puzzle1():
  lines = open("day3.input").read().split("\n")
  zeroCountByPosition = {}
  oneCountByPosition = {}
  for line in lines:
    for i in range(len(line)):
      if line[i] == '0':
        zeroCountByPosition[i] = zeroCountByPosition.get(i, 0) + 1
      if line[i] == '1':
        oneCountByPosition[i] = oneCountByPosition.get(i, 0) + 1
  gammaNumbers = []
  epsilonNumbers = []
  for i in range(len(zeroCountByPosition)):
    if zeroCountByPosition[i] > oneCountByPosition[i]:
      gammaNumbers.append('0')
      epsilonNumbers.append('1')
    else:
      gammaNumbers.append('1')
      epsilonNumbers.append('0')
  gamma = int(''.join(gammaNumbers), 2)
  epsilon = int(''.join(epsilonNumbers), 2)
  return gamma * epsilon



def puzzle2():
  lines = open("day3.input").read().split("\n")
  # oxygen
  oxygen = None
  oxygenCandidates = lines
  for bit in range(len(oxygenCandidates[0])):
    ones = [x for x in oxygenCandidates if x[bit] == '1']
    zeros = [x for x in oxygenCandidates if x[bit] == '0']
    if len(ones) == len(zeros):
      oxygenCandidates = ones
    elif len(ones) > len(zeros):
      oxygenCandidates = ones
    else:
      oxygenCandidates = zeros
    if len(oxygenCandidates) == 1:
      oxygen = int(oxygenCandidates[0], 2)
      break
  # co2
  co2 = None
  co2Candidates = lines
  for bit in range(len(co2Candidates[0])):
    ones = [x for x in co2Candidates if x[bit] == '1']
    zeros = [x for x in co2Candidates if x[bit] == '0']
    if len(ones) == len(zeros):
      co2Candidates = zeros
    elif len(ones) > len(zeros):
      co2Candidates = zeros
    else:
      co2Candidates = ones
    if len(co2Candidates) == 1:
      co2 = int(co2Candidates[0], 2)
      break
  return oxygen * co2


print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())