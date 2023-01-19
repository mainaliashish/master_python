# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# matrix = [[1,2,3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
matrix = [list(range(0,5)), list(range(0,5)), list(range(0,5)), list(range(0,5)), list(range(0,5))]

# print(matrix)
# print(len(matrix))
# Sum of primary diagonal


for i in range(len(matrix)):
    print(matrix[i])

mat_index = 0
sum = 0
for i in range(len(matrix)):
    print(mat_index, len(matrix[i]))
    sum += matrix[i][mat_index]
    mat_index += 1

print(sum)


# pri_sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i] == matrix[j]:
#             pri_sum += matrix[i][j]
#
# print(pri_sum)
#
# sec_sum = 0
# n = 3
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i + j == (n - 1):
#             sec_sum += matrix[i][j]
#
# print(sec_sum)
