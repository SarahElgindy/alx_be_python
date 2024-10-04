class Book:
    def __init__(self,title,author,):
        self.title = title
        self.auther = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"





class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"{title} is either not available or doesn't exist in the library.")

    def return_book(self, title):
        """Mark a book as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"{title} has been returned.")
                return
        print(f"{title} is either already available or doesn't exist in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

