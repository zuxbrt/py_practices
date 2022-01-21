## Rock Paper Scissors   

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

import random;

possible_choices = ['rock', 'paper', 'scissors']
# paper beats rock
# rock beats scissors
# scissors beat paper

while True:

    choice = str(input("Choose rock/paper/scissors (type quit to exit): \n"))
    choice = choice.lower()

    if choice in possible_choices:
        pc_choice = random.choice(possible_choices)
        if pc_choice == choice:
            print("Draw")
        else:

            if pc_choice == "rock":
                if choice == "scissors":
                    print("Lost. " + pc_choice + " beats " + choice + "\n")
                else:
                    print("Win. " + choice + " beats " + pc_choice + "\n")


            if pc_choice == "paper":
                if choice == "rock":
                    print("Lost. " + pc_choice + " beats " + choice + "\n")
                else:
                    print("Win. " + choice + " beats " + pc_choice + "\n")


            if pc_choice == "scissors":
                if choice == "paper":
                    print("Lost. " + pc_choice + " beats " + choice + "\n")
                else:
                    print("Win. " + choice + " beats " + pc_choice + "\n")
        
    else: 
        if choice == 'quit':
            break;
        print('Invalid choice. \n')