usernum1 = int(input("Please enter a number: "))
usernum2 = int(input("Please enter another number: "))

if usernum1 > usernum2:
    print(usernum1, "is larger than ", usernum2)

elif usernum1 == usernum2:
    print(usernum1, ' Is equal to ', usernum2)

else:
    print(usernum1, "is less than ", usernum2)
