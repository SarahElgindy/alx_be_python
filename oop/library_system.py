class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count
    