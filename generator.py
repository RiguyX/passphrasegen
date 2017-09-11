import random
import secrets
dictionary = ["Words", "Should", "Go", "Here", "Agent","Blurt","Center","Difficult","Elite","Forearm","Guerilla"]
while 1==1:
  print("""Would you like to...
  1) Generate a passphrase, or
  2) Edit the generator's vocabulary?""")
  userchoice = input("(Please select 1 or 2): ")
  if userchoice == "1":
    #Allow user to specify minimum and maximum lengths of passphrase and ensure specifications are valid
    while 1==1:
    #  Character length management is currently a disabled feature.
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
    #Actually builds the passphrase from user-defined separators and the variable dictionary
    for i in range(random.randrange(minword, maxword)):
      word = secrets.choice(dictionary)
      passphrase = passphrase + word + separators[random.randint(0, len(separators)-1)]
    passphrase = passphrase + str(random.randint(0, 9))
    print(passphrase)
  else:
    print("""Would you like to...
    1) Add or remove entries,
    2) View the generator's vocabulary, or
    3) Return to the main option select?""")
    userchoice2 = input("(Please select 1, 2, or 3): ")
    if userchoice2 == 1:
      #todo add vocab editor
      print("This feature is not yet implemented. Sorry!")
      continue
    elif userchoice2 == 2:
      for i in dictionary:
        print(i)
      continue
    else:
      continue
