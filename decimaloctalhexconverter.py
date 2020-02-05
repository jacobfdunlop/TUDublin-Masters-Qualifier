usernum = int(input("Please enter a decimal base number: "))
binum = int()
usernum1 = int(usernum)
a =[]
while usernum > 0:
    binum = usernum % 2
    usernum = int(usernum/2)
#   print(binum)

    a.append(binum)
    a.reverse()

print(a, "is the binary conversion")
print(oct(usernum1), "Is the octal conversion")
print(hex(usernum1), "Is he hexadecimal conversion")

