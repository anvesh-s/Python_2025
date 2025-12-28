
import random
random_number = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
computer_choice = random.randint(0,2)


if random_number == 0:
    if computer_choice == 0:
        print("Draw, try again")
    elif computer_choice == 1:
        print("Computer wins")
    else:
        print("You win!")
elif random_number == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Draw, try again")
    else:
        print("Computer wins")
else:
    if computer_choice == 0:
        print("Computer wins")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("Draw, try again")
