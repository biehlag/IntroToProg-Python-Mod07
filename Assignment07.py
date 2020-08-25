# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Error Handling
# ChangeLog (Who,When,What):
# Austin Biehl, 8.24.2020,Created the script

#Demonstrating Pickling

import pickle

print('My Favorite Things')
FavoriteAnimal = str(input('What is your favorite animal?: '))
FavoriteFood = str(input('What is your favorite food?: '))
FavoriteColor = str(input('What is your favorite color?: '))
FavoriteNumber = float(input('What is your favorite number: '))
FavoriteProgrammingLanguage = str(input('What is your favorite programming language?: '))

f = open('favoritethings.dat', 'wb')

pickle.dump(FavoriteAnimal, f)
pickle.dump(FavoriteFood, f)
pickle.dump(FavoriteColor, f)
pickle.dump(FavoriteProgrammingLanguage, f)
pickle.dump(FavoriteNumber, f)

print('\nHere are your favorite things')
f = open('favoritethings.dat', 'rb')
FavoriteAnimal = pickle.load(f)
FavoriteFood = pickle.load(f)
FavoriteColor = pickle.load(f)
FavoriteProgrammingLanguage = pickle.load(f)
FavoriteNumber = pickle.load(f)

print(FavoriteAnimal)
print(FavoriteFood)
print(FavoriteColor)
print(FavoriteProgrammingLanguage)
print(FavoriteNumber)

# Demonstrating Error Handling with ValueError
try:
    FavoriteNumber = float(input('What is 2 + 2?: '))
except ValueError:
    print('Try entering a number!')