class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def __del__(self):
        print(f"Deleting {self.title} of the book")


    def __str__(self):
        return f"(title) by (author), published in (year)"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


