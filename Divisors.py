usernum = int(input('Please enter a number: '))
numlist = [a for a in range(1,usernum) if usernum % a == 0]
print(numlist)
