## Password Generator

# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

import string
import random



def randomUpper():
    """
    Get a random uppercase string.
    """
    return random.choice(string.ascii_uppercase)



def randomLower():
    """
    Get a random lowercase string.
    """
    return random.choice(string.ascii_lowercase)



def randomNumber():
    """
    Get a random number in range of 0 - 9.
    """
    return random.choice(range(0, 9))



def randomCharacter():
    """
    Get a random ascii character.
    """
    return random.choice(string.ascii_letters)



def getWeakPass():
    """
        Generate a weak password (4 characters - uppercase, lowercase, number and random character.)
    """
    upper = randomUpper()
    lower = randomLower()
    number = randomNumber()
    symbol = randomCharacter()
    mix = [upper,lower,str(number),str(symbol)]
    weakpass = ''
    return weakpass.join(mix)



def throwDice():
    return random.choice(range(1,5))



def getStrongPass():
    """
        Generate strong password of 8 characters - including combinations of uppercase, lowercase, number and symbol.
    """

    i = 0
    hasUpper = False    # 1 - dice
    hasLower = False    # 2 - dice
    hasNumber = False   # 3 - dice
    hasChar = False     # 4 - dice

    strongpass = ''

    while i < 7:
        
        # get char type to generate for each iteration individually
        dice = throwDice()

        # uppercase
        if dice == 1:

            # if has uppercase
            if hasUpper:

                # if has all combos, go on
                if hasUpper and hasLower and hasNumber and hasChar:
                    upperChar = randomUpper()
                    strongpass += upperChar

                # avoid repeating same
                else:
                    continue
            
            # append
            else:
                upperChar = randomUpper()
                strongpass += upperChar
                hasUpper = True
            
        # lowercase
        if dice == 2:
            
            # if has lowercase
            if hasLower:

                # if has all combos, go on
                if hasLower and hasUpper and hasNumber and hasChar:
                    lowerChar = randomLower()
                    strongpass += lowerChar

                # avoid repeating same
                else:
                    continue
            
            # append
            else:
                lowerChar = randomLower()
                strongpass += lowerChar
                hasLower = True


        # number
        if dice == 3:
            
                # if has number
            if hasNumber:

                # if has all combos, go on
                if hasNumber and hasUpper and hasLower and hasChar:
                    numberChar = randomNumber()
                    strongpass += str(numberChar)

                # avoid repeating same
                else:
                    continue
            
            # append
            else:
                numberChar = randomNumber()
                strongpass += str(numberChar)
                hasNumber = True

        # character
        if dice == 4:
            
                # if has char
            if hasChar:

                # if has all combos, go on
                if hasChar and hasUpper and hasLower and hasNumber:
                    randomChar = randomCharacter()
                    strongpass += randomChar

                # avoid repeating same
                else:
                    continue
            
            # append
            else:
                randomChar = randomCharacter()
                strongpass += randomChar
                hasChar = True


        i+=1

    return strongpass    



def generate(strength):
    """
        Generate password depending on choosen strength level.
    """
    if strength == 1:
        return getWeakPass()
    if strength == 2:
        return getStrongPass()
            


def main():
    """
        Display prompt for generating password.
    """
    while True:
        choice = int(input("Choose strength type: \n 1. 4 characters - weak password (uppercase, lowercase, numbers, symbols) \n 2. 8 characters - (uppercase, lowercase, numbers, symbols) \n 3. exit \n"))

        if choice not in [1,2,3]:
            print('Invalid choice. \n')
        else:
            if choice == 3:
                break
            res = generate(choice)
            print('=====================================')
            print("Your random password is: " + str(res))
            print('=====================================')
            break





main()