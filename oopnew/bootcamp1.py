class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"

first = input("Enter your first name :")
last = input("Enter your last name :")
age = int(input("Enter your age :"))
thing = input("What do you like? ")
ram = Person(first, last, age)

print("Full Name : {}".format(ram.full_name()))
print(ram.initials())

print(ram.likes(thing))




