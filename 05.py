## list overlap

# write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

b_elements_in_a = []
a_elements_in_b = []

for a_element in a:
    if a_element in b:
        a_elements_in_b.append(a_element)

for b_element in b:
    if b_element in a:
        b_elements_in_a.append(b_element)

print("Elements from list a that are in list b:")
print(*a_elements_in_b)
print("Elements from list b that are in list a:")
print(*b_elements_in_a)