


# if list length is known
a = [11, 33, 50]



b = str(str(a[0]) + str(a[1]) + str(a[2]))

print(b)

# if list length is unknown
string_number = ""

for el in a:
    string_number += str(el)

number = int(string_number)

print(number)
