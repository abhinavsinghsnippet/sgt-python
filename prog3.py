'''3. Calculator Class
•	Create a class named Calculator with methods to perform basic arithmetic operations:
o	add(a, b): Adds two numbers.
o	subtract(a, b): Subtracts one number from another.
o	multiply(a, b): Multiplies two numbers.
o	divide(a, b): Divides one number by another, with a check to prevent division by zero.
•	Instantiate the Calculator class and perform all operations.'''
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calc = Calculator()
print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
