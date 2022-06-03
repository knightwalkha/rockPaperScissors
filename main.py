import random
from secrets import choice
from unittest import result

print('''Welcome to my Rock/ Paper/ Scissor game.
    The rules are simple:
        1. Rock beats Scissors.
        2. Paper beats Rock.
        3. Scissors beats Paper.
''')

while True:
    print('''Make your choice, choosing from the following:
    'R' for Rock
    'P' for Paper
    'S' for Scissors''')

    #taking user inputs/choice
    choice = input('Enter your choice: ')
    
    if choice == 'R':
        user_choice = 'Rock'
    elif choice == 'P':
        user_choice = 'Paper'
    elif choice == 'S':
        user_choice = 'Scissors'
    else:
        print('invalid input')

    #printing user input/choice
    print("You have chosen: " + user_choice)
    print("It's the computers' turn...")

    # Computer chooses randomly any number
	# among 1 , 2 and 3. Using randint method
	# of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
	# is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
	# variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    #printing user input/choice and computer choice
    print("CPU has chosen: " + comp_choice_name)
    print('Player ({}) : CPU ({})'.format(user_choice,comp_choice_name))

    if ((choice == 'R' and comp_choice == 2) or (choice == 'P' and comp_choice == 1)):
        print("Paper wins =>", end = "")
        result = "Paper"
        break
    elif((choice == 'R' and comp_choice == 3) or (choice == 'S' and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
        break
    elif((choice == 'S' and comp_choice == 2) or (choice == 'P' and comp_choice == 3)):
        print("Scissors wins =>", end = "")
        result = "Scissors"
        break
    else:
        print("Game is a tie")

    # Prints if either the user or computer wins
    if result == user_choice:
        print("<== User Wins ==>")
    else:
        print("<== CPU Wins ==>")
    
    print("Do you want to play again? (Y/N)")
    reply = input()


    if reply == 'n' or reply == 'N':
        break

print("Thanks for playing")