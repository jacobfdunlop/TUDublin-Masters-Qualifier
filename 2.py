temp = int(95)
summer = bool(True)

if (temp >= 60) and (temp <= 90) and (summer == (False)):
    party = bool(True)
    print(party)

elif (temp >= 60) and (temp <= 100) and (summer == (True)):
    party = bool(True)
    print(party)

else:
    party = bool(False)
    print(party)

