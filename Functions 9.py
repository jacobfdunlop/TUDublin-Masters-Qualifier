def string_insert(user_str1, user_str2):
    print(user_str1[0:len(user_str1) // 2] + user_str2 + user_str1[len(user_str1) // 2:])


a = input("Please enter a string: ")
b = input("Please enter a string to put inside it: ")

string_insert(a, b)
