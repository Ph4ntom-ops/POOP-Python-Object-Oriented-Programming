# Aggregation                       - It is a relationship where one object (whole) contains
#                                     references to one or more INDEPENDENT objects.


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("The Ultimate Fake Library")

book1 = Book("Don't Believe Everything You Think", "Joseph Nguyen")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("The Power of Your Subconcious Mind", "Joseph Murphy")
book4 = Book("The Alchemist", "Paulo Coelho")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
library.add_books(book4)

print(library.name, end=' ')
print("contains: ")

for book in library.list_books():
    print(book)