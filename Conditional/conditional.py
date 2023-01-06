# x = 10

#
# if(x > 11) :
#     print("{} is greater than 5".format(x))
# elif(x == 10) :
#     print("{} is equal to 10".format(x))
# else :
#     print("{} is not greater than 5".format(x))

# vendors = ["Cisco", "HP", "Dell", "Juniper", "Avaya"]
#
# for each_vendor in vendors :
#     print(each_vendor)
# else:
#     print("The list limit has reached")

# my_string = "Cisco"
#
# for l in my_string:
#     print(l)

# r = range(10)
# for i in r:
#     print(i*2)

# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1

# name = input ("Please enter your name: ")
# age = int(input("Hey, {0}! How old are you? ".format(name)))

# if(age >= 18) :
#     print("You are able to cast vote!")
# else : 
#     print("You need to be 18 years or older to cast vote.")
#     print("Sorry! You still need to wait for {0} years to vote.".format(18-age))


vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print("The entered word is : {}".format(word))
print("Vowels in the entered word is :")
for vowel in found:
    print(vowel)            