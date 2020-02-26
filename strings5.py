s = input("Please enter a string of an odd length: ")
x = 0
while x == 0:
    if len(s) % 2 == 1 and len(s) > 4:
        t = int(len(s) // 2)
        print("middle character: ", s[t])
        print("first half: ", s[0:t], len(s[0:t]), "chars")
        print("second half: ", s[t+1:], len(s[t+1:]), "chars")
        x += 1
    else:
        s = input("Invalid input, Please enter a string of an odd length: ")

