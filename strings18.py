user_str = input("Please enter a word: ")
while user_str != ".":
    vowels = "aeiou"
    if user_str[0] in vowels:
        print(user_str + "yay")
    else:
        for a in range(len(user_str) + 1):
            if user_str[a] in vowels:
                print(user_str[a:] + user_str[0:a] + "ay")
                user_str = "."
                break



