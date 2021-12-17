
DAY_NUMBER=${1:?"Input day number required"}
FILENAME="day${DAY_NUMBER}"

echo Creating templates for day ${DAY_NUMBER}

mkdir -p ${FILENAME}
touch ${FILENAME}/${FILENAME}.input
touch ${FILENAME}/${FILENAME}.example
cat > ${FILENAME}/${FILENAME}.py << EOM
import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  return content

def puzzle1(data):
  # TODO
  return

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("${FILENAME}.example")))
print("puzzle1: ", puzzle1(parse_input("${FILENAME}.input")))
print("example2: ", puzzle2(parse_input("${FILENAME}.example")))
print("puzzle2: ", puzzle2(parse_input("${FILENAME}.input")))
EOM