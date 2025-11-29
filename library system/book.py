# Author: Gourav sen
# Date: 25-11-2025
# Assignment 3 - Library System

class Book:
    def __init__(self, title, author, isbn, available=True, borrow_count=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.borrow_count = borrow_count 

    def borrow(self):
        if self.available:
            self.available = False
            self.borrow_count += 1
            print(f"Book '{self.title}' borrowed.")
            return True
        print(f"Book '{self.title}' is currently unavailable.")
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' returned.")
            return True
        print(f"Error: Book '{self.title}' was not recorded as borrowed.")
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "borrow_count": self.borrow_count
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data.get("title"),
            data.get("author"),
            data.get("isbn"),
            available=data.get("available", True),
            borrow_count=data.get("borrow_count", 0)
        )