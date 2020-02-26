def reverse_second_word(user_str):
    b = []
    a = user_str.split(" ")
    count = 0
    for c in a:
        if count % 2 != 0:
            b.append(c[::-1])
            count += 1

        else:
            b.append(c)
            count += 1



    print(' '.join(b))


string = "One thousand and eighty five hundred million euro"
reverse_second_word(string)
