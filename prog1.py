'''1. Basic Class Creation
•	Create a class called Student with the following attributes:
o	name: Name of the student
o	age: Age of the student
o	grade: Current grade of the student
•	Write a method to display the student’s details.
•	Create three instances of the Student class and display their details.'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Instances of Student class
student1 = Student("Abhinav singh", 19, "12th")
student2 = Student("daksh", 18, "11th")
student3 = Student("garv", 13, "12th")

student1.display_details()
student2.display_details()
student3.display_details()

