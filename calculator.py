
check = bool(False)

while check == (False):

    usernum1 = int(input("Please enter a number: "))
    userop = str(input("Please enter an operator + - * or /: "))
    usernum2 = int(input("Please enter a number: "))

    if userop == "+":
        answer = int(usernum1 + usernum2)

        print(usernum1, "+", usernum2, "=", answer)

    elif userop == "-":
        answer = int(usernum1 - usernum2)
        print(usernum1, "-", usernum2, "=", answer)


    elif userop == "*":
        answer = int(usernum1 * usernum2)
        print(usernum1, "x", usernum2, "=", answer)

    elif userop == "/":
        answer = int(usernum1 / usernum2)
        print(usernum1, "/", usernum2, "=", answer)

    else:
        print("Invalid response. Please Try Again")




