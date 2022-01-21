## list less than ten

# write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

number = int(input("Enter a number: \n"))

n_list = [1,1,2,3,5,8,13,21,34,55,89]
s_list = []
s2_list = []

for element in n_list:
    if(element < 5):
        s_list.append(element)

    if(element < number):
        s2_list.append(element)

    
print("Smaller than five:")
print(*s_list)
print("Smaller than number inputted:")
print(*s2_list)

