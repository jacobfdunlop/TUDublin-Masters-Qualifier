
user_num1 = int(input("Please enter a number:"))
remainder = int(user_num1)
sum = int()
output = []


while remainder > 0:
    remainder = int(user_num1 / 2)
    sum = str(int(user_num1 % 2))
    output.append(sum)

    user_num1 = remainder

output.reverse()
output1 = ''.join(output)

print(output1)

