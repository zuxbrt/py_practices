## character input

# print name and what year the person will reach 100 years from inputted current age and name.

import datetime

name = input("What's your name? \n")
age = int(input("What's your age? \n"))

today = datetime.date.today()
yearsToAdd = 100 - age

targedDate = today.replace(today.year + yearsToAdd)

print("Hey " + name + ", maybe you will be 100 years old " + targedDate.strftime("%Y"));