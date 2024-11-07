'''2. Book Class
•	Create a class named Book with attributes:
o	title: Title of the book
o	author: Author of the book
o	pages: Number of pages
•	Write methods to:
o	Display book details.
o	Check if the book is long (over 300 pages).
•	Create an instance of the Book class and test these methods.'''
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

    def is_long(self):
        return self.pages > 300


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
book1.display_details()
print("Is the book long?", book1.is_long())

