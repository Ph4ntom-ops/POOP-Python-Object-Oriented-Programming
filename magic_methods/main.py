# magic methods                                   - Also known as dunder methods,
#                                                   methods that starts and ends with __ (double underscore)
#                                                   They let you define and customize the behaviour of an object
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):                                  # returns the provided string instead of printing the memory space
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):                                   # checks whether one object's attribute is equal to another object's attribute (without using this dunder method, it will return an error)
        return self.title == other.title

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"The key '{key}' doesn't exist."

book1 = Book("The Alchemist", "Paulo Coelho", 151)
book2 = Book("Atomic Habits", "James Clear", 179)
book3 = Book("The Power of Your Subconcious Mind", "Joseph Murphy", 183)
book4 = Book("Don't Believe Everything You Think", "Joseph Nguyen", 115)

print(book1)
print(book2)
print(book3)
print(book4)

print()

print(book1 == book2)
print(book1 > book4)
print(book3< book2)
print("Atomic Habits" in book2)
print(book4["author"])