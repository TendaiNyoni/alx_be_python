# library_management.py

class Book:
    """Represents a book with a title, author and checked-out state."""

    def __init__(self, title, author):
        self.title = title                # public attribute
        self.author = author              # public attribute
        self._is_checked_out = False      # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned. Return True if successful, False if it was not checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if checkout succeeded, False otherwise (not found or already checked out).
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if return succeeded, False otherwise (not found or wasn't checked out).
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        """Print all available books, one per line in the format: 'Title by Author'."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
