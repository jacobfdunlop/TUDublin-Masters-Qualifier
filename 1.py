cigars = int(70)
weekend = bool(True)

if (cigars >= 40) and (weekend == (True)):
    party = bool(True)
    print(party)

elif (cigars >= 40) and (cigars <= 60) and (weekend == (False)):
    party = bool(True)
    print(party)

else:
    party = bool(False)
    print(party)

