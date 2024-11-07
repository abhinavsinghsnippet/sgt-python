'''11. Person Class with Age Validation
•	Create a class named Person with attributes:
o	name: Name of the person.
o	age: Age of the person.
•	Write methods to:
o	Display the person’s details.
o	Ensure age is set to a positive number.
•	Try creating instances with different age values to see if the validation works.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            print("Error: Age cannot be negative.")
            self.age = 0  
        else:
            self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person("Alice", 25)  
person2 = Person("Bob", -5)    
person3 = Person("Charlie", 30)  

person1.display_details()
person2.display_details()
person3.display_details()
