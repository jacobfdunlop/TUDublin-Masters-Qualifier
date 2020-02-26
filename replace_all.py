def replace_all(user_str, list_1, list_2):
    a = user_str.split(" ")
    output = []
    for word in a:
        if word not in list_1:
            output.append(word)
        elif word in list_1:
            output.append(list_2[list_1.index(word)])

    print(" ".join(output))


d = "This is a wonderful morning"
e = ['is', 'morning']
f = ['was', 'evening']

replace_all(d, e, f)
