#Create a program that ask the user to enter their name and their age . Print out a message addressed to them that tells them the year they will turn 100 years.

name = input('What is your name?: ')
age = int(input('What is your age?: '))
year = int(input('What year we are?: '))

finalage = 100 - age
finalyear = year + finalage

print(f'{name} in the year {finalyear} you will have 100 years')
