# Draw A Game Board  

# Exercise 24

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.


import re


def drawBoard(size):

    dashes = ' --- '
    pipes = '|   '

    for x in range(0, size-1):
        dashes = dashes + '--- '
        pipes = pipes + '|   '

    pipes = pipes + '|'

    for y in range(0,size):
        print(dashes)
        print(pipes) 

    print(dashes)

    return



def main():

    while True:
        choice = str(input('Please type the size of your board (format: NxN): \n'))
        
        if choice == 'quit':
            break

        if choice.find("x") == -1:
            print('Invalid format. \n')
        else:
            choice_splitted = choice.split("x")
           
            if choice_splitted[0] != choice_splitted[1]:
                print('Invalid size. \n')
            else:
                size = int(choice_splitted[0])
                if size < 1 or size > 19:
                    print('Invalid size. \n')
                else:
                    drawBoard(size)
                break



main()