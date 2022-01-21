## odd or even

# ask user for a number. depending on the number - print if the number is even or odd.
# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

x = int(input("type your first number: \n"))
y = int(input("type your second number: \n"))

if(x % 2 == 0):
    print("First number is even.")

if(x == 4):
    print("First number actually is four. Nice.")

if(x / y == x):
    print("Nice job. First number / Second number = First number.")
else:
    print("Oh. So First number / Second number != First number.")