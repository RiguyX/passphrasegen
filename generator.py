import random
import secrets
#Allow user to specify minimum and maximum lengths of passphrase and ensure specifications are valid
while 1==1:
#  minchar = int(input("Minimum Character Length: "))
#  maxchar = int(input("Maximum Character Length: "))
  minword = int(input("Minimum Word Length: "))
  maxword = int(input("Maximum Word Length: "))
  separators = input("Seperators (Multiple Allowed): ")
  if (minword <= maxword) and (minword > 0):
    break
  else:
    print("Input invalid! Make sure minimum lengths are shorter than maximums and are positive numbers!")
    continue
print("This generator is a work in progress, so DON'T USE THIS PASSPHRASE!")
#todo: Use an actual dictionary source for words
passphrase = ""
for i in range(random.randrange(minword, maxword)):
  word = secrets.choice(["Words", "Should", "Go", "Here", "Agent","Blurt","Center","Difficult","Elite","Forearm","Guerilla"]) #THIS IS ONLY AN EXPERIMENTAL LIST!! Do not use this to generate passphrases!
  passphrase = passphrase + word + separators[random.randint(0, len(separators)-1)]
passphrase = passphrase + str(random.randint(0, 9))
print(passphrase)
