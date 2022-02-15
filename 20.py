## Element Search

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

import random

ordered_list = []



def generateList():
    j = 0
    while j < 10:
        number = 0
        if j == 0:
            number = random.randint(0, 10)
        else:
            """ this will generate random numbers in order according to j count"""
            number = random.randint(ordered_list[j - 1], j * 10)

        ordered_list.append(number)
        j+=1



"""
Check if number is in the list.
"""
def check(number):
    if number in ordered_list:
        return True
    else:
        return False



def main():
    n = int(input("Enter a number to see if it's in the list: \n"))

    generateList()

    if check(n) == True:
        print("Number " + str(n) + " is in the list.")
    else:
        print("Number " + str(n) + " is not in the list.")



main()