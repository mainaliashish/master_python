# def compare_str(x, y):
#     return x.lower() == y.lower()
#
# print(compare_str("Abc", "abc"))


def solution(x):
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])

print(solution(-231))
print(solution(345))


def solution(x):
    string = str(x)
    if string[0] == '-':
        strx = string.split("-")[1]
        return int(f"-{strx[::-1]}")
    else:
        return int(string[::-1])

print(solution(-231))
print(solution(345))



array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def move_zeros(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)

    return nums

print(move_zeros(array1))
print(move_zeros(array2))


def prime_numbers(numbers):
    res = []
    for num in range(numbers):
        if num > 1:
            for x in range(2, num):
                if (num % x) == 0:
                    break
            else:
                res.append(num)
    return res

print(prime_numbers(10))

x = [2,6,4,3,1,0]
print('-' * 10)
for i in range(len(x)):
    print(f"Outer loop : {i}")
    for j in range(i+1, len(x)):
        print(f"Inner loop : {i}")
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]

print(x)
