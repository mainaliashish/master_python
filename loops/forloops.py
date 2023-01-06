colors = ['red', 'blue', 'green', 'teal', 'white']

# Appending list with a new Color
# colors.append("black")

# Adding more than one colors
# colors.extend(["violet", "purple"])

# Inserting at specified position
# colors.insert(1, "pink")

# Removing an item from a list -> Expects index 
# colors.pop(1)
# r = range(10)
# lists = list(r)

# for num in lists:
#     print(num)

# While Loop
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

# For Loop
for color in colors:
    print(f"{color}")
    #print("{}".format(color))

# x = len([1,2,4,'a'])
# print(x)