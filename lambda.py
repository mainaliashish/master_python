# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, \
# but can only have one expression.
# lambda arguments: expression

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:

def x(a, b): return a * b
print(x(5, 6))


def x(a, b, c): return a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
