# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call parent constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call parent constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library class
class Library:
    def __init__(self):
        self.books = []  # list to store books

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library"""
        self.books.append(book)

    def list_books(self):
        """Lists all books in the library"""
        for book in self.books:
            print(book)
