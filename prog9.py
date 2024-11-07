'''9. Circle Class with Radius
•	Create a class called Circle with the following attributes:
o	radius: Radius of the circle.
•	Write methods to:
o	Calculate and return the area of the circle.
o	Calculate and return the circumference of the circle.
•	Create instances of Circle, and print the area and circumference for each.
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(5)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())
