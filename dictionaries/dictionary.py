# cat = {"name":"blue", "age":3.5, "isCute":True}
# print(cat["name"])
# print(cat)

# print("\n")


# if "name" in cat:
#     print("Yes")
# else:
#     print("No")

# print("\n")

# cat2 = dict(name="tom", age = 4)
# print(cat2["age"])

# # Iteration in dictionary -> Only Values
# for value in cat.values():
#     print(value)
    
# # Iteration in dictionary -> Only Keys
# for key in cat.keys():
#     print(key)

# for key, value in cat.items():
#     print(f"Key is : {key} and Value is : {value}")
    

# d = dict(a=2, b=3, c=3)
# e = d.copy()
# print(e)


# # creating / generating a dictionary with default values. Multiple assignments
# new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], 'unknown')
# print(new_user)

playlist = {
    'title' : 'patagonia bus',
    'author' : 'colt stelle',
    'songs'  : [
                {'title' : 'song title 1', 'artist':['blue'], 'duration':4.5},
                {'title' : 'song title 2', 'artist':['kitty', 'dj kat'], 'duration':5.2},
                {'title' : 'song title 3', 'artist':['ram'], 'duration':3.5}        
        ]
}

total_duration = 0
for song in playlist['songs']:
    total_duration += song['duration']
    
print("Total song duration : {}".format(total_duration))
