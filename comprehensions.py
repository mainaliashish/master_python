# List comprehension
my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

same_list = [char for char in 'hello']
print(same_list)

my_list_two = [num for num in range(1, 100)]
my_list_two = [num * 2 for num in range(1, 100)]
print(my_list_two)
my_list_three = [num ** 2 for num in range(1, 100) if num % 2 == 0]
print(my_list_three)


# Set comprehension
set_one = {char for char in 'Hello'}
print(set_one)
my_list_two = {num * 2 for num in range(1, 100)}
print(my_list_two)

# Dictionary comprehension
my_dict = {
    'name': 'Jill',
    'age': 20,
    'country': 'nepal'
}

simple_dict = {
    'a': 1,
    'b': 2
}

res = {k: v**2 for k, v in simple_dict.items()}
res = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(res)

my_dict_one = {num: num*2 for num in range(10)}
print(my_dict_one)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
res = [char for char in some_list if some_list.count(char) > 1]
res.sort()
res = set(res)
print(res)

res_one = {char for char in some_list if some_list.count(char) > 1}
print(res_one)