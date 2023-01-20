# def palindrome(n):
#     temp = n
#     rev_num = 0
#     while temp > 0:
#         digit = temp % 10 # 1 # 2
#         rev_num = rev_num * 10 + digit # 0 * 10 + 1 # 1 * 10 + 2
#         temp = temp // 10 # 1232 # 123
#     if n == rev_num:
#         return True
#     return False

# print(palindrome(12321))

# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             print("Fizzbuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# print(fizz_buzz(20))

# def fibo(n):
#     a, b = 0, 1
#     print(a)
#     while b < n:
#         print(b)
#         a, b = b, a+b

# fibo(6)

def fibonnaci(n):
    a, b = 0,1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fibonnaci(6)

def rec_fab(n):
    if n <= 1:
        return n
    else:
        return rec_fab(n-1) + rec_fab(n-2)

n = 10
for i in range(n):
    print(rec_fab(i))