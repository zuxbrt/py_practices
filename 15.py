## Reverse Word Order

# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.

def getReverse(statement):
    splitted = statement.split()
    reversed = ""

    i = len(splitted) - 1
    while i >= 0:
        reversed+= splitted[i] + " "
        i-=1

    return reversed

string = getReverse(input("Type a statement: \n"))
print(string)