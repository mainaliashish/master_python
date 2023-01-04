"""
# Ordered sequence of objects
# a form of data structures
# can contain any collection of items
# like arrays
# List are mutable collection
"""

numbers = [1, 2, 3, 4, 5]
mix_alpha_nums = [1, 2, 3, 'a', 'b', 'z']

print(numbers)
numbers.append(6)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(1, 8)
print(numbers)
print(mix_alpha_nums)

amazon_cart = ['sunglasses', 'notebook', 'watch', 'mobile', 'toys', 'grapes']

# print(amazon_cart[3])
# amazon_cart[3] = 'hat'
print(amazon_cart[1:3])
print(amazon_cart[0::2])
print(amazon_cart[::-1])
amazon_cart.sort()
print(amazon_cart)
# Copy the list to new variable address
new_cart = amazon_cart[:]
new_cart_two = amazon_cart.copy()
print(new_cart)
print(new_cart_two)

# Reference the address of list
new_cart_three = amazon_cart
new_cart_three[1] = 'apple'
print(new_cart_three)
print(amazon_cart)

# Martix

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[1][:2])
print(numbers[2][1])
print(numbers[2][::-1])
print(numbers[1][:-1])
print([numbers[0][2], numbers[1][2], numbers[2][2]])
print(len(numbers))
numbers[0].append(10)
print(numbers)
numbers[2].extend([9, 7, 9])
print(numbers)
print(set(numbers[2]))

x = [1, 2, 3]
# x.pop()
# x.pop(0)
# print(x)
"""
pop() -> removes what item is being removed
remove() -> returns none and item is removed
clear() -> clears the entire list
index() -> returns the position of item in the list
"""

print(4 in x)
print(2 in x)

nums = [1, 2, 3, 4, 5, 2, 3, 4, 5]
print(nums.count(5))

# Common List patterns
print(list(range(1, 20)))

sentence = '-'

new_s = sentence.join(['hello', 'how', 'are', 'you'])

print(new_s)

# List unpacking
basket = [1,2,3,4,5,6,7,8]
a,b,c, *d = basket
print(a, b, c)
print(d)

m = None
print(m)