# Fundamental Data types in Python
"""
1. int
2. float
3. bool
4. list
5. tuple
6. set
7. dict
8. complex
"""

print(2)
print(type(3))
print(type(5/3))
print(type(1.0))
print(round(3.56))
print(abs(-30))

# Operator Precedence
# PEMDAS
# 1. ()
# 2. **
# 3. *
# 4. /
# 5. +
# 6. -

print(3 * (4 - 1))
print(5 + 1 - 2)

print(bin(5))
print(bin(5).replace("0b", ''))
print(hex(10))
print(int('0b101', 2))

print("*" * 20)

user_iq = 190
print(f"User IQ : {user_iq}")

# [start:end:stepover]

selfish = '01234567'
print(selfish[1:])
print(selfish[::-1])
print(selfish[:5])
print(selfish[::1])

# strings in python are immutable
# selfish[3] = '7'  -- Error

print(len(selfish))
print(selfish.count('7'))


greet = 'Hellooooooo'

print(greet[::])
print(greet[:])
print(len(greet))

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.title())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())
quote_two = quote.replace('be', 'me')
print(quote_two)
print(quote)

# Booleans : bool
# True or False

name = "Ashish Mainali"
# age = 27
relationship_status = 'single'
is_cool = True

# user_age = int(input("Enter your age : "))
# born_year = int(input("Enter your birth year : "))
# age = 2023 - born_year
# print(f"Your age is {age}")
# print(age == user_age)

# Password checker

password = 'ashish@'
username = input("Enter your username : ")
password = input("Enter your password : ")
password_length = len(password)
replaced_password = password_length  * '*'
print(f"Hey, {username}! Your Password, {replaced_password}, \
        is {password_length} characters long.")












