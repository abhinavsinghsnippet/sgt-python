'''6. Employee Class
•	Create an Employee class with the following attributes:
o	name: Employee name.
o	salary: Salary of the employee.
•	Write methods to:
o	Display employee information.
o	Give a raise by a certain percentage.
•	Create multiple employees, give them raises, and display their updated details.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"New salary after raise: {self.salary}")


emp1 = Employee("Abhinav singh", 50000)
emp2 = Employee("garv", 60000)
emp1.give_raise(10)
emp2.give_raise(5)
emp1.display_info()
emp2.display_info()
