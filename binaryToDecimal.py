user_num = input("Please Enter a binary number: ")

length = int(len(user_num))
power = ()
x = int()
z = int()
output = int()

while length >= 0:

    z = int(user_num[length - 1])
    if z == 1:
        power = (2 ** x) * z
        x += 1
        length -= 1
        output += power

    else:
        x += 1
        length -= 1

print("Binary Number: ", user_num)
print(" Decimal Output: ", output)
