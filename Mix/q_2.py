# Sort a list without using a sort keyword

my_list = [1,2,3,4,20,9,8,10]

n = len(my_list)

for i in range(n):
    for j in range(i+1, n):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]


print(my_list)

new_list = []

while my_list:
    min = my_list[0]
    for number in my_list:
        if min > number:
            min = number
    new_list.append(min)
    my_list.remove(min)

print(new_list)
