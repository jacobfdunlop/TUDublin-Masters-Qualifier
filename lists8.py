def not_in(a, b):
    for c in a:
        for d in b:
            if c == d:
                a.remove(d)

    print(a)


sample_list = [1, 2, 3, 4, 5, 6]
sample_list_2 = [10, 9, 8, 7, 6]
not_in(sample_list, sample_list_2)

