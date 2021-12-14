import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  points, folds = content.split("\n\n")
  points = [[int(x) for x in p.split(",")] for p in points.split("\n")]
  folds = folds.split("\n")
  folds = [x.replace("fold along ", "").strip().split("=") for x in folds]
  folds = [[x[0], int(x[1])] for x in folds]
  return points, folds


def draw_points(points):
  width = max([p[0] for p in points]) + 1
  height = max([p[1] for p in points]) + 1
  image = [["." for i in range(width)] for j in range(height)]
  for p in points:
    image[p[1]][p[0]] = "#"
  return "\n" + "\n".join([" ".join(r) for r in image])


def puzzle1(data):
  points, folds = data
  axis, axisVal = folds[0]
  if axis == "x":
    visible = set()
    for p in points:
      if p[0] < axisVal:
        visible.add(tuple(p))
      else:
        visible.add((axisVal - (p[0] - axisVal), p[1]))
    return len(visible)
  else:
    visible = set()
    for p in points:
      if p[1] < axisVal:
        visible.add(tuple(p))
      else:
        visible.add((p[0], (axisVal - (p[1] - axisVal))))
    return len(visible)

def puzzle2(data):
  points, folds = data
  for axis, axisVal in folds:
    if axis == "x":
      visible = set()
      for p in points:
        if p[0] < axisVal:
          visible.add(tuple(p))
        else:
          visible.add((axisVal - (p[0] - axisVal), p[1]))
      points = visible
    else:
      visible = set()
      for p in points:
        if p[1] < axisVal:
          visible.add(tuple(p))
        else:
          visible.add((p[0], (axisVal - (p[1] - axisVal))))
      points = visible
  return draw_points(points)

print("example1: ", puzzle1(parse_input("day13.example")))
print("puzzle1: ", puzzle1(parse_input("day13.input")))
print("example2: ", puzzle2(parse_input("day13.example")))
print("puzzle2: ", puzzle2(parse_input("day13.input")))
