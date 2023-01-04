# Hash table
# key value pairs
# unordered
# represented by {}

dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
}

print('a' in dictionary.keys())
print(dictionary.get('a'))
print(dictionary.get('x', False))
# for item, val in dictionary.items():
#     print(item, val)

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1980,
    "colors": ["red", "white", "blue"]
}

# NOTE Duplicate keys not allowed
print(my_dict)
print(len(my_dict))
print(my_dict["brand"])


# Another way to define dictionary in python

new_dict = dict(name="John", age=36, country="Norway")
print(new_dict)
# Ways to add items in a dictionary
# 1 Using update({}) method
new_dict.update({'job': 'Programmer'})
print(new_dict)
# 2 method
new_dict['language'] = 'Python'
print(new_dict)

# Removing an item from a dictionary
age = new_dict.pop('age')
print(f"Age : {age}")
print(new_dict)

# The popitem() method removes the last inserted item
x = new_dict.popitem()
print(x)
print(new_dict)
