#print("First module name is {}".format(__name__))

# name   = input('What is your name? ')
# color  = input('What is your favorite color? ')
# print(name + " likes " + color)
# print("{} likes {}".format(name, color))

# birth_year = input('Enter your birth year :')
# age = 2019 - int(birth_year)
# print("Your present age is {}".format(age))


# weight_lbs = input('Enter your weight in pound :')
# weight_kg = int(weight_lbs) * 0.45
# print('{} pounds into Kg is {}'.format(weight_lbs, weight_kg) )

# course = "Python for Beginners"

# name = "John"
# last = "Smith"
# message = name + " [" + last + "] " + " is a coder"
# print(message)

# course = "Python for Beginners"
# print('Python' in course)

# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))

is_hot = False
is_cold = False

day = input("What kind of day it is? ")
day = day.lower()

if day == 'hot':
    is_hot = True
elif day == 'cold':
    is_cold = True

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day.")   
    
print("Enjoy Your day.")