# the result of the function is same
# given the same input the output will always be the same
# should not produce any side-effects
# Try to create pure functions as possible

def multiply(li: list):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply([1, 2, 3]))

wizard = {
    'name': 'Jose',
    'power': 50
}

def attack(character):
    pass