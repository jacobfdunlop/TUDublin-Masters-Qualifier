count = int()

table_num = 1

for a in range(11):
    a = a * 9
    print(count, "x 9 = ", a)
    while table_num < 11:
        print(count, " x ", table_num, "=", count*table_num)
        table_num += 1
    table_num = 1
    count += 1
    print()

