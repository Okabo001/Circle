class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    # Create a Circle object with radius 5
    c = Circle(5)

    # Compute the area of the circle
    print("Area:", c.area())

    # Compute the perimeter of the circle
    print("Perimeter:", c.perimeter())