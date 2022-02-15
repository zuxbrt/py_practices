# File Overlap  
# Exercise 23
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.


import requests

prime_numbers_link = "https://www.practicepython.org/assets/primenumbers.txt"
happy_numbers_link = "https://www.practicepython.org/assets/happynumbers.txt"

prime_numbers = []
happy_numbers = []

"""
    Retrieve numbers from link.
"""
def getNumbers(link, list):
    r = requests.get(link, stream=True)

    for line in r.iter_lines():
        if line: 
            decoded = line.decode('ascii')
            list.append(decoded)



def main():
    getNumbers(prime_numbers_link, prime_numbers)
    getNumbers(happy_numbers_link, happy_numbers)

    overlapList = []
    for elem in prime_numbers:
        if elem in happy_numbers:
            overlapList.append(elem)

    print(overlapList)



main()