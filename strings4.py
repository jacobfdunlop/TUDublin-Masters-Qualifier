my_str = input("Please enter a string: ")
x = 0
while x == 0:
    if int(len(my_str)) > 4:
        print(my_str[0:2] + my_str[-2] + my_str[-1])
        x = 1

    else:
        print("Please try again")
        my_str = input("Please enter a string: ")
