# numbers = list(range(10))
#
# for index, item in enumerate(numbers):
#     print(index, item)
#
#
# x, y, *z = [1,2,3,4,5]
#
# print(z)

letters = ['a', 'b', 'c', 'd']

# Adding items to list objects

# append() -> adds item to the last of list
letters.append('e')

# insert() -> can add item to specific index
letters.insert(0, 'A')

# pop() -> removes item from the last of list
letters.pop()

# remove() -> can remove item from a specific index of list
# letters.remove("A")
#
#
# items = [
#     ("Product 2", 2),
#     ("Product 4", 4),
#     ("Product 1", 1),
# ]
#
# items.sort(key= lambda item:item[1])
#
# item_prices = [item[1] for item in items]
# print(item_prices)
#
# item_sort_price = [item[1] for item in items if item[1] >= 2]
# print(item_sort_price)
# print(items)

values = [x * 2 for x in range(1,10)]
values_one = (x * 2 for x in range(1,10))

print(type(values))
print(type(values_one))

for x in values:
    print(x)


for i in *values:
    print(i)
