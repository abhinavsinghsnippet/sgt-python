'''5. Library Management
•	Create a class called Library with attributes:
o	library_name: Name of the library.
o	books: A list to store the books available in the library.
•	Write methods to:
o	Add a book to the library.
o	Remove a book from the library.
o	Display all books in the library.
•	Create a Library instance, add books, remove a book, and list all available books.'''
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed from the library.")
        else:
            print(f"{book} not found in the library.")

    def display_books(self):
        print(f"Books in {self.library_name}: {self.books}")


library = Library("City Library")
library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.remove_book("The Catcher in the Rye")
library.display_books()
