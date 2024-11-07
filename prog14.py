'''14. Course Enrollment System
•	Create a Course class with attributes:
o	course_name: Name of the course.
o	students: A list of enrolled students.
•	Write methods to:
o	Enroll a student.
o	Remove a student.
o	Display the list of students enrolled in the course.
•	Create instances of the Course class, enroll students, and display the list.
'''
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
      
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} has been enrolled in {self.course_name}.")
        else:
            print(f"{student_name} is already enrolled in {self.course_name}.")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from {self.course_name}.")
        else:
            print(f"{student_name} is not enrolled in {self.course_name}.")

    def display_students(self):
        if self.students:
            print(f"Students enrolled in {self.course_name}: {', '.join(self.students)}")
        else:
            print(f"No students are currently enrolled in {self.course_name}.")

course1 = Course("Mathematics")
course1.enroll_student("Abhinav singh")
course1.enroll_student("garv")
course1.enroll_student("daksh")
course1.display_students()

course1.remove_student("garv")
course1.display_students()
