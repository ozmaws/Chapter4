myString = "string"
reversedString = ""
length = int(len(myString) - 1)

while length >= 0:
  reversedString += myString[length]
  length -= 1

print(reversedString)
