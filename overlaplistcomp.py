a = [1, 4, 7, 12, 34, 56, 5, 19, 100]
b = [3, 7, 56, 50, 4, 100, 1025, 83]
c = [y for y in b for x in a if x == y]

print(c)
