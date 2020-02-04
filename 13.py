usernum = int(input("Please enter a number: "))

sum = 0
for divisor in range(1, usernum):
    if usernum % divisor == 0:
        sum += divisor

if sum == usernum:
    print("Perfect number")

elif sum < usernum:
    print("deficient number")

else:
    print("abundant number")

print(usernum, divisor, sum)
