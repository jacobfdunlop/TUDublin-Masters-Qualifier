# operations

plus = "Addition: 1 + 1"
minus = 'Subtraction: 2 - 1'
multiplication = 'Multiplication: 1 * 2'
float_division = 'Float Division: 2 / 1'
integer_division = 'Integer Division: 2 // 1'
exponents = 'Exponents (powers): 2 ** 2'
modulo = 'Modulo (remainders): 2 % 2'
assignment = "Assignment: ="
equals = "Equals: =="
increment = "Increment: +="
reduced_by = "Reduce by: -="
multiplied_by = "Multiply by: *="

operations = [plus, minus, multiplication, float_division, integer_division, exponents, modulo, assignment, equals, increment, reduced_by, multiplied_by]
# operations in brackets will always be done first


# boolean logic
boolean_logic = "Boolean logic is a binary True/ False logic system. You can create a bool type and assign it true  \n" \
                "or false. Boolean logic is also how if/else statements work. They check to see if a condition is true or false and then \n" \
                "execute certain blocks of code on that basis."


# for example
def boolean_logic_example(a, b):
    print(boolean_logic)
    a = int(input("please enter an integer: "))
    b = int(input("please enter an integer: "))

    if a < b:
        print("2 is less than 5")

    elif a == b:
        print("2 is equal to 5")

    else:
        print("5 is less than 2")


# loops
loop_choice = input("Do you want to know about loops? y/n: ")
if loop_choice == "y":
    for_loop = "A for loop is a loop which iterates through a list, string or any data structure \n" \
               "which contains multiple elements and can perform operations on them \n \n "

    def for_loop_example(a):
        print(for_loop)
        print()
        a = int(input("Enter a range for the For loop to iterate through: "))
        for num in range(a + 1):
            if num % 2 == 0:
                print(num, "is an even number")
            else:
                print(num, "is an odd number")
        print()


    for_loop_choice = input("Do you want to know about for loops? y/n: ")
    if for_loop_choice == 'y':
        for_loop_example(0)

    # while loop

    while_loop = "A while loop repeatedly runs a block of code and \n" \
                 "checks if a condition is true or false. Once the condition is \n" \
                 "met, the loop stops."


    def while_loop_example(a, b):
        print(while_loop)
        print()
        a = int(input("please enter a low number: "))
        b = int(input("please enter a higher number: "))
        while a <= b:
            print("a: ", a)
            print("b: ", b)
            print()
            a += 1
            if a == b:
                print("a = b : loop complete")


    while_loop_choice = input("Do you want to know about while loops? y/n: ")
    if while_loop_choice == "y":
        while_loop_example(0, 0)
# strings

strings = "Strings are a data type in python which function as a list of ASCI characters. \n\n" \
          "Strings can be concatenated using + and can be split using .split. \n\n" \
          "String indexes operate the same as lists. 0 is the first index and -1 is the last. \n\n "

string_choice = input("Do you want to know about strings? y/n: ")

if string_choice == "y":
    print(strings)
    # splitting strings
    my_string = "hello I am Jacob Dunlop"
    split_string_list = my_string.split(" ")
    print("The string: ", my_string, ": can be split using my_string.split and becomes: ", split_string_list)
    print()
    print("If you type my_string[::2] you get every second character like so: ", my_string[::2])
    print()
    print("To find the last character in a string you would type my_string[-1] like so: ", my_string[-1])
    print()
    print("You can concatenate two characters from a string: my_string[0] + my_string[3] = ", my_string[0] + my_string[3])
    print()
    print("You can also use the strip function to remove all incidents of a character in a string using my_string.strip('a')")
    print()
    print("And lastly you can count the incidence of a character in a string using my_string.count('a')")
    print()

functions_choice = input("Do you want to know about functions? y/n: ")

if functions_choice == "y":

    print("Functions are created using def. \n"
          "so def my_function(a,b) creates a function called my_function which takes parameters a and b. \n"
          "\n"
          "This makes code reusable and allows users to simplify large blocks of code into one single line. \n"
          "You can print a function if you return something within the code of the function. \n"
          "You can also include a print command inside your function.")


list_choice = input("Do you want to know about lists? y/n :")

if list_choice == "y":
    print("Lists are a data structure used in python to store variables. \n\n"
          "Lists can be changed, sorted, called upon, iterated through and are useful for many tasks. \n\n"
          "List indexes work much the same as strings: \n\n"
          "my_list[0:5:2] would print the items in my_list starting at the first index going to the 6th index, iterating over every second item. ")

    print()
    list_choice_2 = input("Do you want to see some list methods? y/n: ")
    if list_choice_2 == "y":
        list_functions = ["my_list.append(a)", "my_list.extend(a)", "my_list.insert(a)", "my_list.index(0)", "my_list.reverse()", "my_list.pop(2)", "my_list.sort()"]
        print(list_functions)
        print()


operations_choice = input("Do you want to check some of the operations in python? y/n: ")

if operations_choice == 'y':
    for a in operations:
        print(a)

print()
print("good luck!")
