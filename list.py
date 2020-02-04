list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []
usernum = int(input('Please enter the maximum number: '))

for element in list1:
    if element < usernum:
        {
         list2.append(element)

        }
print("old list: ", list1)
print("new list: ", list2)

#one line solution for making a new list from the elements of the original list which are less than the user input
print([aa for aa in list1 if aa < usernum])
