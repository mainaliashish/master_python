for item in [1, 2, 3, 4, 5]:
    for x in ['a', 'b', 'c']:
        print(f"{item} - {x}")

# Iterable
# Collection of data types that can be iterated over
# can be list, tuple, dictionary, set, string
# NOTE : int objects are not iterable

user = {
    'name': 'Ashish',
    'age': 100,
    'can_swim': False
}

# Dictionary methods and patterns

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# most common pattern
for key, value in user.items():
    print(f"{key} - {value}")

# for i in 50:
#     print(i)

# Simple counter example

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for i in my_list:
    count += 1

print(f"Total items count (using iteration) : {count}")
print(f"Total item count (using len method): {len(my_list)}")

sum = 0
for i in my_list:
    print(f"{sum} + {i} = {sum + i}")
    sum += i

print(sum)

# Range function
# range(start, end, step)
# does not include upper limit

print(range(10))
print(range(0, 10))

# for _i in range(0, 10):
#     print(_i + 1)

for i in range(10, 1, -2):
    print(i)

for _ in range(2):
    print(list(range(10)))

# enumerate

for i in enumerate(['a', 'b', 'c']):
    print(i)

i = 0
while i < 40:
    print(i)
    i += 1
else:
    print('done with all the work..')

# while True:
#     response = input("Say something : ")
#     if response == 'bye':
#         print("Goodbye!")
#         break

my_list = [1,2,3]
start = 0
while start < len(my_list):
    print(my_list[start])
    start += 1

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*'
empty = ' '
for pixels in picture:
    for pixel in pixels:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print()

# Check duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)

print(duplicates)