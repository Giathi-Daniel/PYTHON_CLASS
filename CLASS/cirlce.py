class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def Area(self):
        return 3.14 * self.radius * self.radius

    def Perimeter(self):
        return 3.14 * self.diameter

cir = Circle(7)
print(cir.radius)
print(cir.diameter)
print(cir.Area())
print(cir.Perimeter())