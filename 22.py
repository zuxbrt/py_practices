# Read From File 
# Exercise 22
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. 
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. 
# To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


import requests

link = "https://www.practicepython.org/assets/Training_01.txt"

categories = {}

"""
    Count categories from parsed link content.
"""
def parseTextFile():
    r = requests.get(link, stream=True)

    for line in r.iter_lines():
        if line: 
            decoded = line.decode('ascii')
            line_contents = decoded.split('/')

            currentCategory = line_contents[2]
            if currentCategory in categories:
                categories[currentCategory] += 1
            else:
                categories[currentCategory] = 1


def main():
    parseTextFile()

    print("\nCount of categories:")
    print("=======================")
    for category, count in categories.items():
        print(category + " -> " + str(count))
    print("=======================")

main()