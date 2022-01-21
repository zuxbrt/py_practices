## List Overlap Comprehensions

# Take two lists, say for example these two:
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension.

import random

a = random.sample(range(1, 100), 5)
b = random.sample(range(1, 100), 5)

unique = [x for x in a for y in b if x in b if y in a]

print(*a)
print(*b)
print(*unique)


