# Data structures are way of organising data in a computer memory

# Built-in data structures

# List
# Tuples
# Sets
# Dictionary

letters = ["a", "b", "c"]

for _ in range(len(letters)):
    item = letters.pop()
    print(f"Removing item : {item}")

print(f"Final List : {letters}")

# zeros = [0] * 6
# print(zeros)

vowels = ["a", "e", "i", "o", "u"]

print(vowels[0])
print(vowels[-1])
print(vowels[0:3])
print(vowels[:]) # returns the copy of the original List

# print(zeros + vowels)
#
# print(list(range(10)))
#
# chars = list("Hello World")
# print(chars)
# print(len(chars))
