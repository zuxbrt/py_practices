## string lists - palindrome

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Type your word: \n"))
word_r = ""

index = 1

for letter in word:
    word_r += (word[len(word) - index])
    index+=1

if word_r == word:
    print("Your word is a palindrome.")
else: 
    print("Your word is not a palindrome.")