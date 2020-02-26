def kaprekar(a):
    # create list for kaprekar numbers
    kaprekar_list = []

    # create for loop
    for c in range(10, a):
        # create variable for square
        user_num_sq = int(c) ** 2

        # convert to string
        user_num_sq = str(user_num_sq)

        # find the halfway point of the squared number
        split_ind = len(user_num_sq) // 2

        # find the two halves of the split
        d = int(user_num_sq[:split_ind])
        e = int(user_num_sq[split_ind:])

        f = int(user_num_sq[:split_ind + 1])
        g = int(user_num_sq[split_ind + 1:])

        # compare to see if kaprekar
        if d + e == int(c):
            kaprekar_list.append(d + e)

        elif f + g == int(c):
            kaprekar_list.append(f + g)

    print(kaprekar_list)


user_num = int(input("Please enter a number: "))

kaprekar(user_num)
