#explanation
#
#so in order to decipher it id have to use question 2 page 109 in order to create the algorithm
# id have to use the range of 33-126

text = ""
distance = 1
encryptedText = "12345"
possibilities = 126 - 33
while possibilities > 0:
  for i in encryptedText:
    value = ord(i)
    cipherValue = value - distance
    if cipherValue < ord('!'):
      cipherValue = (ord('~') - (distance + (ord('!') - value - 1)))
    text += chr(int(cipherValue))
  possibilities -= 1
  distance += 1
  print(str(distance-1) + ". " + str(text))
  text = ""
