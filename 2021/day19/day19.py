import os
import numpy as np
from collections import Counter
from tqdm import tqdm

ROTATION_MAPPER = [
  lambda x, y, z: (x,y,z),
  lambda x, y, z: (x,z,-y),
  lambda x, y, z: (x,-y,-z),
  lambda x, y, z: (x,-z,y),
  lambda x, y, z: (-x,y,-z),
  lambda x, y, z: (-x,z,y),
  lambda x, y, z: (-x,-y,z),
  lambda x, y, z: (-x,-z,-y),
  lambda x, y, z: (y,x,-z),
  lambda x, y, z: (y,z,x),
  lambda x, y, z: (y,-x,z),
  lambda x, y, z: (y,-z,-x),
  lambda x, y, z: (-y,x,z),
  lambda x, y, z: (-y,z,-x),
  lambda x, y, z: (-y,-x,-z),
  lambda x, y, z: (-y,-z,x),
  lambda x, y, z: (z,x,y),
  lambda x, y, z: (z,y,-x),
  lambda x, y, z: (z,-x,-y),
  lambda x, y, z: (z,-y,x),
  lambda x, y, z: (-z,x,-y),
  lambda x, y, z: (-z,y,x),
  lambda x, y, z: (-z,-x,y),
  lambda x, y, z: (-z,-y,-x),
]

def rotate_positions(array, rotation_fn):
  return np.array([rotation_fn(*pos) for pos in array])

def identical_rows(array):
  for i in range(len(array)-1):
    if not np.array_equal(array[i], array[i+1]):
      return False
  return True

def calibrate(source_positions_calibrated, scannerN_positions):
  """
  Find the position of scanner N and return a calibrated scanner N position
  Return (success, [scanner_position, calibrated_positions]) pairs
  """
  counter = Counter()
  # count all possible distance diffs
  for x in source_positions_calibrated:
    for y in scannerN_positions:
      diff = x - y
      counter[tuple(diff)] += 1
  # we found it if we have at least 12 of the same diffs
  relative_pos, count = counter.most_common(1)[0]
  if count >= 12:
      scannerN_positions_calibrated = scannerN_positions + relative_pos
      return True, [relative_pos, scannerN_positions_calibrated]
  return False, []

def find_common_rows(array1, array2):
  array1 = set([tuple(x) for x in array1])
  array2 = set([tuple(x) for x in array2])
  return array1.intersection(array2)

def find_beacons(source_positions_calibrated, scannerN_positions):
  for rotation_fn in ROTATION_MAPPER:
    scannerN_alt = rotate_positions(scannerN_positions, rotation_fn)
    success, val = calibrate(source_positions_calibrated, scannerN_alt)
    if success:
      scannerN_positions_calibrated = val[1]
      print(find_common_rows(source_positions_calibrated, scannerN_positions_calibrated))
      return val
  return None

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  content = content.split("\n\n")
  sections = []
  for section in content:
    section = section.strip().split("\n")
    assert section[0].startswith("---")
    rows = [x.split(",") for x in section[1:]]
    rows = [[int(x) for x in row] for row in rows]
    sections.append(np.array(rows))
  return sections

def calibrateScanners(data):
  calibratedPositions = {0: data[0]}
  relataivePositions = {0: (0,0,0)}
  with tqdm(total=len(data)) as pbar:
    while True:
      for i in range(len(data)):
        if i not in calibratedPositions:
          nonCalibrated = data[i]
          for j in list(calibratedPositions.keys()):
            calibrated = calibratedPositions[j]
            for rotation_fn in ROTATION_MAPPER:
              rotated = rotate_positions(nonCalibrated, rotation_fn)
              success, val = calibrate(calibrated, rotated)
              if success:
                relataivePositions[i] = val[0]
                calibratedPositions[i] = val[1]
                pbar.update()
      if len(calibratedPositions) == len(data):
        break
  return calibratedPositions, relataivePositions

def puzzle1(data):
  calibratedPositions, _ = calibrateScanners(data)
  beacons = set()
  for i in range(len(calibratedPositions)):
    beacons = beacons.union([tuple(pos) for pos in calibratedPositions[i]])
  return len(beacons)


def puzzle2(data):
  _, relataivePositions = calibrateScanners(data)
  relataivePositions = list(relataivePositions.values())
  largestDistance = -1
  for i in range(len(relataivePositions)):
    for j in range(len(relataivePositions)):
      if i != j:
        dist = abs(relataivePositions[i][0] - relataivePositions[j][0])
        dist += abs(relataivePositions[i][1] - relataivePositions[j][1])
        dist += abs(relataivePositions[i][2] - relataivePositions[j][2])
        largestDistance = max(largestDistance, dist)
  return largestDistance

print("example1: ", puzzle1(parse_input("day19.example")))
print("puzzle1: ", puzzle1(parse_input("day19.input")))
print("example2: ", puzzle2(parse_input("day19.example")))
print("puzzle2: ", puzzle2(parse_input("day19.input")))


