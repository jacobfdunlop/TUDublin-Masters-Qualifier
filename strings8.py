import random
my_str = input("Please enter a string for encryption: ")
y = int(random.randint)

for a in my_str:
    if a != " ":
        x = int(ord(a))
        print(chr(x + 1), end="")

    else:
        x = int(ord(a))
        print(chr(y), end="")




