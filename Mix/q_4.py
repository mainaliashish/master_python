products = {
    112: 'Grapes',
    98: 'Apple',
    222: 'Orange',
    10: 'Banana'
}

res = { key: value for key, value in sorted(products.items(), key=lambda x: x[0]) }
print(res)


# d = sorted(products.keys())
# dict = {}
#
# for i in d:
#     print(d[i])

# print(dict)

# Find fibonacci using recursion
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

for i in range(10):
    print(recur_fibo(i))

# print(recur_fibo(10))


# Find the factorial of number
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

# Reversing the string
s = "the sky is blue"
l = s.split()
print(l)
t = 5
x = []
for letter in range(len(l)):
    x.append(l[len(l) - t])
    t += 1
print(x)
# l = l[::-1]
# l = " ".join(l)
# print(l)


s = "Hello how are you?"
ch = {}

for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1

print(ch)



nums = [1,20,3,40,5,6]
maximum = nums[0]
minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(minimum)
print(maximum)


power = lambda x : x ** 2

print(power(4))


try:
    10 / 0
except ZeroDivisionError as e:
    print(e)


def reverse(x):
    output = ""
    for c in x:
        output = c + output

    return output


print(reverse("Hello"))


x = [4,12,9,5,6]
y = [4,9,12,6]
missing = 0
for n in x:
    if n not in y:
        missing = n

print(missing)

z = x[:]
for n in y:
    if n in z:
        z.remove(n)

print(z)

# x = set(x)
# y = set(y)
#
# print(x-y)
