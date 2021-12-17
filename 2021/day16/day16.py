import os
from functools import reduce

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
    return {"version": version, "packetType": packetType, "value": value}, rest
  lengthIdType, rest = consumeOperatorLengthTypeId(rest)
  if isTotalLengthInBits(lengthIdType):
    numOfBits, rest = getNumberOfBits(rest)
    packetBits, rest = rest[:numOfBits], rest[numOfBits:]
    packets = []
    while len(packetBits) > 0:
      res, packetBits = decodePacket(packetBits)
      packets.append(res)
    return {"version": version, "packetType": packetType, "packets": packets}, rest
  else:
    # number of subpackets
    numOfSubPackets, rest = getNumberOfSubPackets(rest)
    packets = []
    for i in range(numOfSubPackets):
      res, rest = decodePacket(rest)
      packets.append(res)
    return {"version": version, "packetType": packetType, "packets": packets}, rest

def sumVersions(result):
  versionSum = result.get("version", 0)
  if "packets" in result:
    for p in result["packets"]:
      versionSum += sumVersions(p)
  return versionSum


def puzzle1(data):
  result = []
  for hexStr in data:
    context = hexStr if len(hexStr) < 20 else "omitted"
    result.append((sumVersions(decodePacket(hexToBinary(hexStr))[0]), context))
  return result

def computeValue(packet):
  packetType = packet["packetType"]
  if packetType == 4:
    return packet["value"]
  subPacketValues = [computeValue(p) for p in packet["packets"]]
  if packetType == 0:
    return sum(subPacketValues)
  elif packetType == 1:
    return reduce(lambda x, y: x*y, subPacketValues)
  elif packetType == 2:
    return min(subPacketValues)
  elif packetType == 3:
    return max(subPacketValues)
  elif packetType == 5:
    if subPacketValues[0] > subPacketValues[1]:
      return 1
    return 0
  elif packetType == 6:
    if subPacketValues[0] < subPacketValues[1]:
      return 1
    return 0
  elif packetType == 7:
    if subPacketValues[0] == subPacketValues[1]:
      return 1
    return 0
  raise RuntimeError(f"Unknown packet type {packetType}")

def puzzle2(data):
  result = []
  for hexStr in data:
    packet, _ = decodePacket(hexToBinary(hexStr))
    context = hexStr if len(hexStr) < 20 else "omitted"
    result.append((computeValue(packet), context))
  return result

print("example1: ", puzzle1(parse_input("day16.example1")))
print("puzzle1: ", puzzle1(parse_input("day16.input")))
print("example2: ", puzzle2(parse_input("day16.example2")))
print("puzzle2: ", puzzle2(parse_input("day16.input")))


