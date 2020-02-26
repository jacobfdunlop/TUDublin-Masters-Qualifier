import random

my_str = input("Please enter a string: ")
a = int(random.randint(0, len(my_str)) - 1)

b = int(random.randint(0, len(my_str)) - 1)

if a == b:
    b = int(random.randint(0, len(my_str)) - 1)


if a != b:

    if a > b:
        c = my_str[:b]
        e = my_str[b+1:a]
        d = my_str[a+1:]

        z = (c + my_str[a] + e + my_str[b] + d)
        if len(z) == len(my_str):
            print(z)

    else:
        c = my_str[:a]
        e = my_str[a+1:b]
        d = my_str[b+1:]

        z = (c + my_str[b] + e + my_str[a] + d)
        if len(z) == len(my_str):
            print(z)
