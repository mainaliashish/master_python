
# If Conditional loop in Python
name = input("Please enter your name:")
age = int(input("How old are you, {0} ?".format(name)))
print(age)

if age >= 18:
    print("Congratulation, You are old enough to vote!")
    print("Please, put an X in the ballet box.")
else:
    print("please come back in {0} years.".format(18 - age))


# print("please guess a number between 1-10: ")
# guess = int(input())

# if guess < 5 :
#     print("Please guess a higher number")
#     guess = int(input())
#     if guess == 5 :
#         print("Well done! You guessed it.")
#     else:
#         print("Sorry! Your guess did not match")
# elif guess > 5 :
#     print("Please guess a lower number")
#     guess = int(input())
#     if guess == 5 :
#         print("Well done! You guessed it.")
#     else:
#         print("Wrong guess")
# else:
#     print("You got it first time!")

# age = int(input("How old are you? "))
# #if (age >= 16) and (age <= 65) :
# #if 16<= age <= 64:
#     # print("Have a good day")
#
# if (age < 16) or (age > 64):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day at work!")

# x = "true"
# if x:
#     print("x is true")
# else:
#     print("x is false")

# i = 0
# while i < 10:
#     print("i is now {0}".format(i))
#     i = i + 1


# For Loop in python

# emails = ['ashishmianalee@gmail.com', 'ram@test.com', 'codelover@gmail.com']
#
# for email in emails:
#     if 'gmail' in email:
#         print(email)


# String Manipulation Using Python

# c = "Hi There!"

# print(c[0:2])
# print(c[0:4])
# print(c[-3:])

# s = "hello"
# # Creating List
# c = ["H", 12, 22, "Hello World"]
#
# print(c[2])
# print(c[:2])
#
# c.append("new list item")
# print(c)
#
# c.reverse()
# print(c)


# Defining a Function in Python
# def currency_converter(rate, currency):
#     dollars = rate * currency
#     return dollars
#
#
# r = float(input("Enter Rate : "))
# c = float(input("Enter Euros : "))
#
#
# total = currency_converter(r, c)
# print("Total amount : $ {}".format(total))


# While Condition

# password = ""
# while password != "Python3":
#     password = input("Enter Password : ")
#     if password == "Python3":
#         print("You are logged in!")
#     elif password == "":
#         print("Please enter password")
#     else:
#         print("Password does not match")
#


# Multiple For Loops

# names = ["Ram", "John", "Hari", "Shyam"]
# cities = ["Jhapa", "Pokhara", "Kathmandu", "Palpa"]
# ages  = [12, 14, 15, 18]
#
# for name, age, city in zip(names, ages, cities) :
#     print("Name : {0} , Age : {1} and City : {2}".format(name, age, city))