ab_string = 'abababababab'
new_string = (ab_string[::2])
print(new_string)

for a in range(len(ab_string)):
    if ab_string[a] == 'a':
        print(ab_string[a], end='')


