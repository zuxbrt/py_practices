## List Remove Duplicates 

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

list1 = set()

def formSet():
    
    i = 5
    while i > 0:
        number = int(input('Type number: (' + str(i) + ") remaining \n"))
        list1.add(number)
        i-=1
        
    list2 = []
    for element in list(list1):
        if(element in list2):
            list2.remove(element)
        else:
            list2.append(element)

    print(*list2)

formSet()