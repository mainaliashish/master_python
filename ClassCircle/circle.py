class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


radius = int(input("Enter the radius of circle :"))
circle = Circle()
area_of_circle = circle.set_radius(radius)
print("Area of circle with radius {} is {}".format(radius, circle.area()))
















