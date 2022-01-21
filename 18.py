## Cows And Bulls Solutions

#Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. 
# Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place,
#  they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random


def compare(number, take):
    cows_bulls = [0,0]
    for i in range(len(number)):
        if number[i] == take[i]:
            cows_bulls[1]+=1
        else:
            cows_bulls[0]+=1
    return cows_bulls



def main():

    isPlaying = True

    number = str(random.randint(0, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while isPlaying:
        guess = input("Guess the number pal! \n")

        if(guess == "exit"):
            break
            
        results = compare(number, guess)
        guesses+=1

        print("You have "+ str(results[0]) + " cows, and " + str(results[1]) + " bulls.")

        if results[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again. \n")

main()