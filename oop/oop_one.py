class Human:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self) -> str:
        return f"Human name is {self.first} {self.last}"

    def __str__(self) -> str:
        return f"{self.first} {self.last}"

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that."

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return "You can't do that"

human = Human("Ashish", "Mainali", 27)
# human1 = Human("Ashish1", "Mainali", 27)
print(human)
# print(human + human1)
print(human * '3')
