
DAY_NUMBER=${1:?"Input day number required"}
FILENAME="day${DAY_NUMBER}"

echo Creating templates for day ${DAY_NUMBER}

mkdir -p ${FILENAME}
touch ${FILENAME}/${FILENAME}.input
cat > ${FILENAME}/${FILENAME}.py << EOM
import os

def parse_input():
  input_filepath = os.path.join(os.path.dirname(__file__), "${FILENAME}.input")
  return open(input_filepath).read().split("\n")

def puzzle1():
  lines = parse_input()
  # TODO
  return



def puzzle2():
  lines = parse_input()
  # TODO
  return


print("puzzle1: ", puzzle1())
print("puzzle2: ", puzzle2())
EOM