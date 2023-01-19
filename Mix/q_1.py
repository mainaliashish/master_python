# Generate an infinite fibonacci series using generator

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

func = fibonacci()

print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
