class User():

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        if self.age >= 65:
            return f"{self.first} is a senior citizen"


if __name__ == '__main__':

    # first = input("Enter your first name :")
    # last = input("Enter your last name :")
    # age = int(input("Enter your age :"))
    # user1 = User(first, last, age)
    # print(user1.full_name())
    # print(user1.likes("Ice Cream"))
    # print(user1.is_senior())

    ashish = User.from_string("Ashish, Mainali, 25")
    print(ashish.full_name())
