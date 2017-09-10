import random
import secrets
#Allow user to specify minimum and maximum lengths of passphrase and ensure specifications are valid
#todo: Allow user to specify spaces between words
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
print("Input valid. The actual generator is a work in progress, so DON'T USE THIS PASSPHRASE!")
#todo: Use an actual dictionary source for words, implement character length checker, add space characters, add numbers
passphrase = ""
for i in range(random.randrange(minword, maxword)):
  word = secrets.choice(["Agent","Blurt","Center","Difficult","Elite","Forearm","Guerilla"]) #THIS IS ONLY AN EXPERIMENTAL LIST!! Do not use this to generate passphrases!
  passphrase = passphrase + word + separators[random.randint(0, len(separators)-1)]
passphrase = passphrase + str(random.randint(0, 9))
print(passphrase)
