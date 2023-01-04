# unordered collection of unique objects
# set object does not support indexing

my_set = {1, 2, 3, 4, 5, 6, 6, 5}

my_set.add(100)
print(my_set)

x = [1, 2, 3, 4, 5, 5]
print(set(x))
print(1 in my_set)
print(my_set)
print(len(my_set))

set_one = {1, 2, 3, 4}
set_two = {3, 4, 5, 6}

print(set_one.difference(set_two))
# Union
print(set_one.union(set_two))
print(set_one | set_two)
# Interaction
print(set_one.intersection(set_two))
print(set_one & set_two)
print(set_one.isdisjoint(set_two))
my_set.discard(6)
print(my_set)