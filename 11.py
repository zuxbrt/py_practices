# Check Primality Functions

# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def isPrime(number):
    isPrime = False

    for i in range(2, number):
        if (number % i) == 0:
            isPrime = True
            break
    
    return isPrime


def getNumber():
    number = int(input("Type your number: \n"))
    if number > 1:
        return number
    else:
        print(str(number) + ' cannot be a prime number.')


x = getNumber()

result = isPrime(x)
if result:
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")
