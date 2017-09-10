#Allow user to specify minimum and maximum lengths of passphrase and ensure specifications are valid
if 1==1:
  minchar = int(input("Minimum Character Length: "))
  maxchar = int(input("Maximum Character Length: "))
  minword = int(input("Minimum Word Length: "))
  maxword = int(input("Maximum Word Length: "))
  if (minchar <= maxchar) and (minword <= maxword) and (minchar > 0) and (minword > 0):
    break
  else:
    print("Input invalid! Make sure minimum lengths are shorter than maximums and are positive numbers!")
#todo generate passphrase according to user's specs
