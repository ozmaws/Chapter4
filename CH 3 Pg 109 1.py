#letter a
text = "python"
distance = 3
encryptedText = ""
for i in text:
  value = ord(i)
  cipherValue = value + distance
  if cipherValue > ord('z'):
    cipherValue = ord('a') + distance - (ord('z') - value + 1)
  encryptedText += chr(int(cipherValue))
print(encryptedText)

#letter b
text = "hacker"
distance = 3
encryptedText = ""
for i in text:
  value = ord(i)
  cipherValue = value + distance
  if cipherValue > ord('z'):
    cipherValue = ord('a') + distance - (ord('z') - value + 1)
  encryptedText += chr(int(cipherValue))
print(encryptedText)

#letter c
text = "wow"
distance = 3
encryptedText = ""
for i in text:
  value = ord(i)
  cipherValue = value + distance
  if cipherValue > ord('z'):
    cipherValue = ord('a') + distance - (ord('z') - value + 1)
  encryptedText += chr(int(cipherValue))
print(encryptedText)
