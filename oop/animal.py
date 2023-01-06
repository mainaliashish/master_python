class Animal(object):
    def __init__(self):
        print("Animal Created")
        
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")


# Inheritence from Animal class
class Dog(Animal):
    
    def __init__(self):
        #Animal.__init__(self) # Base class constructor initialization
        print("Dog Created..")

    # Method Overriding
    def whoAmI(self): 
        print("I am a dog..")

    def eat(self):
        print("Dog is eating..")



if __name__ == '__main__':
    animal = Dog()
    
    animal.whoAmI()
    animal.eat()