def divide(x, y):
    try:
        return f"{x} divide by {y} is {x/y}"
    except ZeroDivisionError as e:
        return e
    except TypeError:
        return 'Both numbers must be int or floats'


print(divide(1, 2))
print(divide(1, 0))
print(divide(1, '2'))
