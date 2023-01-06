# map()
# map(function, iterable)

from functools import reduce


def multiply_by_two(x):
    return x * 2


y = map(multiply_by_two, [1, 2, 3])
print(list(y))

# filter()
# filter(function, iterable)


def check_odd(num):
    return num % 2 != 0


my_list = list(range(1, 15))
z = filter(check_odd, my_list)
print(list(z))

# zip()
# zip(iterable_one, iterable_two, *)

list_one = list(range(1, 10, 2))
list_two = list(range(1, 10, 3))
list_three = zip(list_one, list_two)
print(list(list_three))

# reduce()

my_list = [1, 2, 3, 4, 5]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
