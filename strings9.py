river = "Mississippi"
target = input('Input a chracter to find: ')
for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index", index)
        break



print("Letter", target, "not found in river", river)
