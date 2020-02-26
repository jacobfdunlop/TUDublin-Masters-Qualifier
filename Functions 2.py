def even_num_range(user_num):
    for a in range(user_num + 1):
        if a % 2 == 0:
            print(a, " is even")

        else:
            print(a, " is odd")


even_num_range(10)
