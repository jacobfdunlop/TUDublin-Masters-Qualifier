def begin_with(a, b):
    count = 0
    for c in a:
        if c[0] == b:
            count += 1
    print(count)


my_list = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
my_letter = input("Please enter a character: ")

begin_with(my_list, my_letter)
