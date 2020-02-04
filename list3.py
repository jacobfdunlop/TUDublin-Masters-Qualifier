userage = int(input("Please enter your year of birth: "))
brotherage= int(input("Please enter your brother's year of birth: "))
sisterage= int(input("Please enter your sister's year of birth: "))
motherage= int(input("Please enter your mother's year of birth: "))
fatherage= int(input("Please enter your father's year of birth: "))

yearsofbirth = [a for a in range(2020) if a == userage or a == brotherage or a == sisterage or a == motherage or a == fatherage ]
print("Your family's birth years are: ", yearsofbirth)
