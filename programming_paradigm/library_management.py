# library_management.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Return whether the book is checked out."""
        return self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Represents a library that manages books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
