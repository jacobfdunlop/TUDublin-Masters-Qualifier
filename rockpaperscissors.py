check = bool(False)
while check == False:
    player1 = input("Player 1 - Please enter Rock(r), Paper(p) or Scissors(s). r/p/s: ")
    player2 = input("Player 2 - Please enter Rock(r), Paper(p) or Scissors(s). r/p/s: ")

    if player1 == "r" and player2 == "s":
        print("Player 1 wins")


    elif player1 == "r" and player2 == "p":
        print("Player 2 wins")


    elif player1 == "p" and player2 == "r":
        print("Player 1 wins!")


    elif player1 == "p" and player2 == "s":
        print("Player 2 wins!")


    elif player1 == "s" and player2 == "p":
        print("Player 1 wins!")


    elif player1 == "s" and player2 == "r":
        print("Player 2 wins!")


    else:
        print("It's a draw!")

    playagain = input("Do you want to play again? y/n: ")
    if playagain == "n":
        break

print("Thanks for playing")

