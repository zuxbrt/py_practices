# Write To A File 
# Exercise 21
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:
# Ask the user to specify the name of the output file that will be saved.



"""
    Write contents to file.
"""
def writeTofile(contents, filename):
    with open(filename + ".txt", "w") as opened_file:
        opened_file.write(contents)
    print('Content saved to ' + filename + '.txt ')


def main():
    contents = str(input("Enter text you wish to write in the file: \n"))
    nameOfFile = str(input("Enter filename for inputted text to be saved:\n"))
    writeTofile(contents, nameOfFile)


main()