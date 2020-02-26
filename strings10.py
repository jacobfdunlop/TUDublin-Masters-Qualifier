import string

s1 = input("Enter a string: ")
s1_modified = s1.lower()
bad_chars = string.whitespace + string.punctuation

# define ints and bool
x = int()
y = int(1)
z = bool()


# iterate through string
for a in s1_modified:

    # where the first letter is the same as the last letter,
    # and the second letter is the same as the second last
    # letter etc continue through the loop and return z = True
    if s1_modified[x] == s1_modified[-y]:
        x += 1
        y += 1
        z = True

    # otherwise exit the string with z = false and end the program
    else:
        z = False
        break


# if z then it is a palindrome else it is not
if z:
    print("This is a palindrome")

else:
    print("this is not a palindrome")


