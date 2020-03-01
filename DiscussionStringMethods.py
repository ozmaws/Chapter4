header = "Im sorry ive been playing skyrim recently"
print(header.center(10))
print("-----------------------------")
s = str("Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.")
print("Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.")
len(s)
print("")
print("There are " + str(len(s)) + " letters in your sentence.")
print("")
Num = s.count(' ') + 1
print("There are " + str(Num) + " words in your sentence.")
print("")
if s.endswith("."):
    print("This sentence ends with a period.")
else:
    print("This sentence does not end with a period.")
print("")
if s.isalpha():
    print("There are only alphabetical symbols in this sentence.")
else:
    print("This sentence is not comprised of only alphabetical symbols.")
print("")


    



