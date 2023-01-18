# The basic syntax
# try:
# except:

# try:
#     foobar
# except NameError as err:
#     print(err)


def my_func(d, key):
    try:
        return d[key]
    except KeyError:
        return f"No key matching '{key}' in the hashmap"
        # return -1

my_dict = { 'name': 'Tom' }

res = my_func(my_dict, 'city')
print(res)

while True:
    try:
        number = int(input("Enter a number to guess : "))
        if number == 7:
            print("Yay, You guessed the correct number")
            break
    except ValueError:
        print("Not a valid decimal number")


