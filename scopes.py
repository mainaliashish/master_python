# Scope : what variables do I have accessed to?
# Scopes are functional in python i.e functional scope
'''
    # Step 1 : Start with Local
    # Step 2 : Parent Local?
    # Step 3 : Global
    # Step 4 : Built-in python function
'''

name = 'Jane'

def print_name():
    name = 'Mike'
    print(name)

total = 0
def count():
    global total
    total += 1
    return total

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print(f"inner x : {x}")

    inner()
    print(f"outer x : {x}")

if __name__ == '__main__':
    print_name()
    print(name)
    print(count())
    print(count())
    print(count())

    outer()