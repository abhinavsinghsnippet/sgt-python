'''. School Class with Student Management
•	Create a class called School with attributes:
o	school_name: Name of the school.
o	students: A list to store students enrolled in the school.
•	Write methods to:
o	Add a student to the list.
o	Remove a student from the list by name.
o	Display the names of all enrolled students.
•	Instantiate a School class, add students, remove one, and display the list of students.
'''
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} added to the school.")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} removed from the school.")
        else:
            print(f"{student_name} not found.")

    def display_students(self):
        print(f"Students in {self.school_name}: {self.students}")

school = School("Greenwood High")
school.add_student("Alice")
school.add_student("Bob")
school.remove_student("Alice")
school.display_students()
