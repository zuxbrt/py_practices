## Guessing Game One

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

import random

number = random.randint(1, 10)

while True:
    guess = input("Guess the number (type exit to exit):")

    if(guess == "exit"):
        break;

    guess = int(guess)

    if(guess == number):
        print("You guessed the number! - " + str(number))
        break;
    if(guess > number):
        print("Too high.")
    if(guess < number):
        print("Too low.")