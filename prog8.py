'''8. Car Class with Mileage
•	Create a Car class with attributes:
o	make: The make of the car.
o	model: The model of the car.
o	year: The year of manufacture.
o	mileage: The current mileage of the car.
•	Write methods to:
o	Display car details.
o	Update the mileage.
o	Check if the car qualifies as an “old” car (older than 10 years).
•	Create instances of the Car class and test these methods.
'''
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")

    def update_mileage(self, new_mileage):
        self.mileage = new_mileage
        print(f"Mileage updated to: {self.mileage}")

    def is_old(self):
        return (2024 - self.year) > 10

# Instance of Car class
car1 = Car("Toyota", "Camry", 2010, 120000)
car1.display_details()
car1.update_mileage(125000)
print("Is the car old?", car1.is_old())
