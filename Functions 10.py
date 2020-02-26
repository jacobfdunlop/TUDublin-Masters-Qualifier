def text_delete(user_str, r1, r2):
    print(user_str[:r1] + user_str[r2:])


a = input("Please enter a string: ")
b = int(input("Please enter start of range: "))
c = int(input("Please enter end of range: "))

text_delete(a, b, c)
