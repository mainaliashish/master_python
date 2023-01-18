# syntax [___ for ___ in ___]
# List comprehension

y = [x*10 for x in range(10)]
print(y)

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

name = "ashish"

upper_names = [char.upper() for char in name]
print(upper_names)

friends = ['ram', 'hari', 'sita']

friends_new = [friend.title() for friend in friends]
print(friends_new)

nums = [1, 2, 3, 4, 5, 6]
str_nums = [str(num) for num in nums]
print(str_nums)

numbers = list(range(1, 7))
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
# print(list(set(numbers) - set(evens)))
print(evens)
print(odds)

with_vowels = "This is much fun."

without_vowels = "".join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)

# Nested List

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(len(nested_list))

for i in nested_list:
    for j in i:
        print(j)

# Nested list comprehension
print("*" * 20)
[[print(j) for j in i] for i in nested_list]

board = [[ num for num in range(1,4) ] for val in range(1,4)]
print(board)





