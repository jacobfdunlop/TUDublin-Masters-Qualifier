def even_only(a):
    c = []
    a.sort()
    for b in a:
        if b % 2 == 0:
            c.append(b)

    print(c)


my_list = [1, 2, 67, 34, 89, 100, 23, 12, 26, 74]

even_only(my_list)
