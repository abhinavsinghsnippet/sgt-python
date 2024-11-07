'''7. Rectangle Class
•	Create a class called Rectangle with attributes:
o	length: Length of the rectangle.
o	width: Width of the rectangle.
•	Write methods to:
o	Calculate and return the area of the rectangle.
o	Calculate and return the perimeter of the rectangle.
•	Create instances of Rectangle, calculate their area and perimeter, and print the results.
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect1 = Rectangle(10, 5)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
