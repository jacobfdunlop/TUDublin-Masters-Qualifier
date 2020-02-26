def first_last(user_str):
    if len(user_str) > 4:
        user_str = user_str[:2] + user_str[-2:]
        print(user_str)

    else:
        print("invalid entry")


a = (input("Please enter a string: "))
first_last(a)
