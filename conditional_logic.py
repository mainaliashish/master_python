is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You\'re old enough to drive.")
elif is_licensed:
    print("You can drive.")
else:
    print("You are still young to drive.")

# Truthy and Falsy
print(bool(1))
print(bool(0))
print(bool(None))
print(bool({}))
print(bool([]))

# Ternary Operator
# condition_is_true if condition else condition_is_false

print('You can drive.') if is_old else print('No, you can\'t drive')

is_friend = True
can_message = "message is allowed" if is_friend else "message is not allowed"
print(can_message)

# Short circuiting

is_friend = True
is_user = False

print(is_friend and is_user)
print(is_friend or is_user)

# Logical Operators
# and, or, not
print('a' > 'b')
print(f"{ord('a')} - {ord('b')} { ord('a') > ord('b') }")
print('A' < 'a')
print(ord('A'))
print(ord('a'))
print(ord('b'))


is_magician = True
is_expert = False

# Check if magician and expert
if is_magician and is_expert:
    print('Expert')
elif is_magician and not is_expert:
    print('at least getting there')
elif not is_magician:
    print('need magic power')
else:
    pass

# is checks for exact address in the memory
print(1 == True)
print(1 is True)

print([] == [])
print([] is [])

print(10 == 10.0)
print(10 is 10.0)

