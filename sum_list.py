def sum_of(a):
    b = [a for a in range(a)]
    print(sum(b), "is the sum of", a)


y = int(input("Please enter a number: "))
sum_of(y)
