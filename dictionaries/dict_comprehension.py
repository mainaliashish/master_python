#{ ___:___ for ___ in ___  }

numbers = {
    'first': 1,
    'second': 2,
    'third': 3
}

res = { key: val ** 2 for key, val in numbers.items() }
print(res)

squares = { num: num **2 for num in [1,2,3,4,5] }
print(squares)

str1 = ["A", "B", "C"]
str2 = [1,2,3]

res = { str1[i] : str2[i] for i in range(len(str1)) }
print(res)

info = { "name": 'ashish', 'address':'reading', 'origin': 'nepal' }

info_upper = { k.title():v.title() for k,v in info.items() }
print(info_upper)


num_list = [1,2,3,4,5]
res = { num: ('even' if num % 2 == 0 else 'odd') for num in num_list }
print(res)
