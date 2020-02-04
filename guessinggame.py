# import the random module
import random

check = 0
# create the random number calling on the random module and giving a range of 1-9
comp_num = random.randint(1, 9)

# create a counter to increment each them they make a guess.
guess_num = 0

while check == 0:
    # take user input for a guess.
    user_num = int(input("Please enter a guess between 1 and 9: "))

    # test if guess is higher than number
    if user_num > comp_num:
        print("Too high")
        guess_num += 1

    # test if guess is lower than number
    elif user_num < comp_num:
        print("Too Low")
        guess_num += 1

    # test if guess is equal to number
    elif user_num == comp_num:
        print("Correct")
        guess_num += 1

        # tell them how many guesses they needed
        print("You needed ", guess_num, "guesses")

        # ask if they want to play again
        guess_num = 0
        replay = input("Do you want to play again? y/n: ")

        if replay == "y":
            comp_num = random.randint(1,9)


        if replay == "n":
            break




    # if the input was invalid, this was an invalid guess
    else:
        print("Invalid guess")

# exit text

print("Thanks for playing")
