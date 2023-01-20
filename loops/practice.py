# if __name__ == '__main__':
#     N = int(input())
#     list = []
#     for i in range(N):
#         user_input = input()
#         res = user_input.split()
#         if res[0] == 'insert':
#             list.insert(int(res[1]), int(res[2]))
#         if res[0] == 'remove':
#             list.remove(int(res[1]))
#         if res[0] == 'append':
#             list.append(int(res[1]))
#         if res[0] == 'print':
#             print(list)
#         if res[0] == 'sort':
#             list.sort()
#         if res[0] == 'pop':
#             list.pop()
#         if res[0] == 'reverse':
#             list.reverse()

# Complete the solve function below.
# def cap(x):
#     if not x.isdigit():
#         return x.capitalize()


# def solve(s):
#     res = s.split()
#     final = []
#     for word in res:
#         if not res.isdigit():
#             word.capitalize()
#         final.append(word)
#     return "".join(final)


# string = 'bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd'
# split = 9
# x=[]
# y = 0

# for s in range(len(string)):
#     x.append(string[y:split])
#     y = split
#     split += 9
#     if string[y:split] == '':
#         break

# print("\n".join(x))


def print_formatted(number):
    pad = number
    for i in range(1, number+1):
        d = str(i).rjust(pad)
        o = str(oct(i)[2:]).rjust(pad)
        h = str(hex(i)[2:]).upper().rjust(pad)
        b = str(bin(i)[2:]).rjust(pad)
        print(d, o, h, b)
    return


print_formatted(10)