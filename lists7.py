def no_doubles(a):
    for b in a:
        for d in a:
            if b == d:
                a.remove(d)

    print(a)


sample_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
no_doubles(sample_list)

