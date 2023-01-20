if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        user_input = input()
        res = user_input.split()
        if res[0] == 'insert':
            list.insert(int(res[1]), int(res[2]))
        if res[0] == 'remove':
            list.remove(int(res[1]))
        if res[0] == 'append':
            list.append(int(res[1]))
        if res[0] == 'print':
            print(list)
        if res[0] == 'sort':
            list.sort()
        if res[0] == 'pop':
            list.pop()
        if res[0] == 'reverse':
            list.reverse()
