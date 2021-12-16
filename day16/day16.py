import os

def parse_input(filename):
  content =  open(os.path.join(os.path.dirname(__file__), filename)).read()
  return content.split("\n")

def binaryToDecimal(binary):
  return int(binary, 2)

def hexToBinary(hexStr):
  result = bin(int(hexStr, 16))
  result = result.replace("0b", "")
  result = result.zfill(len(hexStr) * 4)
  return result

def consumeVersion(s):
  return binaryToDecimal(s[:3]), s[3:]

def consumePacketType(s):
  return binaryToDecimal(s[:3]), s[3:]

def isLiteralValue(packetType):
  return packetType == 4

def consumeLiteralValues(s):
  result = []
  while len(s) > 0:
    cur, s = s[:5], s[5:]
    result.append(cur[1:])
    if cur[0] == "0":
      break
  return binaryToDecimal("".join(result)), s

def consumeOperatorLengthTypeId(s):
  return s[0], s[1:]

def isTotalLengthInBits(lengthIdType):
  return lengthIdType == "0"

def getNumberOfBits(s):
  return binaryToDecimal(s[:15]), s[15:]

def getNumberOfSubPackets(s):
  return binaryToDecimal(s[:11]), s[11:]


def decodePacket(binStr):
  version, rest = consumeVersion(binStr)
  packetType, rest = consumePacketType(rest)
  if isLiteralValue(packetType):
    value, rest = consumeLiteralValues(rest)
    return {"version": version, "value": value}, rest
  lengthIdType, rest = consumeOperatorLengthTypeId(rest)
  if isTotalLengthInBits(lengthIdType):
    numOfBits, rest = getNumberOfBits(rest)
    packetBits, rest = rest[:numOfBits], rest[numOfBits:]
    packets = []
    while len(packetBits) > 0:
      res, packetBits = decodePacket(packetBits)
      packets.append(res)
    return {"version": version, "packets": packets}, rest
  else:
    # number of subpackets
    numOfSubPackets, rest = getNumberOfSubPackets(rest)
    packets = []
    for i in range(numOfSubPackets):
      res, rest = decodePacket(rest)
      packets.append(res)
    return {"version": version, "packets": packets}, rest

def sumVersions(result):
  versionSum = result.get("version", 0)
  if "packets" in result:
    for p in result["packets"]:
      versionSum += sumVersions(p)
  return versionSum


def puzzle1(data):
  result = []
  for hexStr in data:
    result.append((sumVersions(decodePacket(hexToBinary(hexStr))[0]), hexStr))
  return result

def puzzle2(data):
  # TODO
  return

print("example1: ", puzzle1(parse_input("day16.example")))
print("puzzle1: ", puzzle1(parse_input("day16.input")))
print("example2: ", puzzle2(parse_input("day16.example")))
print("puzzle2: ", puzzle2(parse_input("day16.input")))


