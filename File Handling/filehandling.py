file = open("/home/ashish/pythonprograms/File Handling/example.txt", 'r')

contents = file.read()

print(contents)

print()

file.seek(0)
c = file.readlines()
new_content = [i.rstrip("\n") for i in c]
print(new_content)

file.close()


# Writing in File
# file = open("example1.txt", 'w')
# data = ["Line 5", "Line 6", "Line 7", "Line 8"]
#
# for d in data:
#     result = file.write(d + "\n")
#     if result:
#         print("Success {} inserted".format(d))
#     else:
#         print("Fail")
#
# file.close()


# Appending in File
# file = open("example1.txt", 'a')
# data = ["Line 5", "Line 6", "Line 7", "Line 8"]
#
# for d in data:
#     result = file.write(d + "\n")
#     if result:
#         print("Success {} inserted".format(d))
#     else:
#         print("Fail")
#
# file.close()

