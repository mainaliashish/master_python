# class Sample(object):
#     def __init__(self, name):
#         self.name = name

# if __name__ == '__main__':
#     x = Sample("Ashish")
#     print(x.name)


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_sum = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        print(j)
        if i == j:
            diagonal_sum += mat[i][j]

print(diagonal_sum)

# mat_index = 0
# sum = 0
# print(len(mat))
# for i in range(len(mat)):
#     # print(mat_index, len(mat[i]))
#     sum += mat[i][mat_index]
#     mat_index += 1

# print(sum)


# mat = [
#     [1, 2, 5],
#     [4, 5, 6],
#     [7, 8, 9]]

# sec_sum = 0
# n = 3
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if i + j == (n - 1):
#             sec_sum += mat[i][j]

# # 1 + 1 == 3 - 1 : 2

# print(sec_sum)


# x = [1,2,3]
# y = [1,2,3]
# res = []
# for xnum in range(len(x)):
#     for ynum in range(len(y)):
#         if xnum == ynum:
#             res.append(x[xnum] + y[ynum])

# print(res)


def column_sum(lst):
    res = []
    for i in range(0, len(lst)):
        s = 0
        for j in range(0, len(lst[i])):
            # s += lst[j][i]
            s += lst[i][j]
        res.append(s)
    return res


# Driver code
lst = [[1, 5, 3],
       [2, 7, 8],
       [4, 6, 9]]
print(column_sum(lst))
