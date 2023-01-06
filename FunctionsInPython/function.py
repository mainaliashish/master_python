# def add_two_num(x, y) :
#     """
#     Docstring comment..
#     This is a simple function to add two integer numbers..
#     """
#     result = x + y
#     return result
#
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
#
# print("The sum of {} and {} is {}".format(a,b,add_two_num(a, b)))

# class Sample():
#     pass
#
# x = Sample()
# print(type(x))

# class Dog():

#     # Class object attributes
#     species = "mammal"

#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name  = name
#         pass


# mydog = Dog("Lab", "Tommy")
# hisdog = Dog("Husky", "Jhonny")
# print(mydog.breed + " " + mydog.name + " " + mydog.species)
# print(hisdog.breed + " " + mydog.name)


# dynamic arguments passing..
def sum_all_nums(*args):
    """
    [summary]
    This is a function that expects integers 
    (at least one argument)
    Returns:
    [type] -- [description]
    Returns sum of integers  passed in the argument
    """
    total = 0
    for num in args:
        total += num
    return total
    
result = sum_all_nums(1, 2, 3, 4, 5)
print(result)
# print(sum_all_nums.__doc__)


# def ensure_correct_info(*args):
#     if "ashish" in args and "mainali" in args:
#         print("welcome back")
#     else:
#         print("Identity miss matched")

# ensure_correct_info(1, "ashish", "mainali", "Dudhe")

def favorite_colors(**kwargs):
    for person, color in kwargs.items(): 
        # Iteration on dictionary (Key, Values)
        print(f"{person}'s favorite color is {color}")


favorite_colors(ram='red', shyam='blue', sita='green', hari='violet')



            

