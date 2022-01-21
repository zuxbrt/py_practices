## divisors

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

x = int(input("Type your number: \n"))

x_range = range(2, x)

for element in x_range:
    if x % element == 0:
        print('Number ' + str(element) + " is a divisor of " + str(x))


