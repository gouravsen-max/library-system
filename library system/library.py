import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, title, author, isbn):
        if self.find_book(isbn):
            print(f"Error: Book with ISBN {isbn} already exists.")
            return False
            
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_data()
        return True

    def register_member(self, name, member_id):
        if self.find_member(member_id):
            print(f"Error: Member with ID {member_id} already exists.")
            return False
            
        new_member = Member(name, member_id)
        self.members.append(new_member)
        self.save_data()
        return True

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            result = member.borrow_book(book)
            if result:
                self.save_data()
            return result
        print("Error: Member or book not found for lending.")
        return False

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            result = member.return_book(book)
            if result:
                self.save_data()
            return result
        print("Error: Member or book not found for returning.")
        return False

    def most_borrowed_book(self):
        if not self.books:
            return None
        return max(self.books, key=lambda b: b.borrow_count)

    def borrowed_books_count(self):
        cnt = 0
        for b in self.books:
            if not b.available: 
                cnt += 1
        return cnt

    def save_data(self):
        books_data = [b.to_dict() for b in self.books]
        members_data = [m.to_dict() for m in self.members]
        
        try:
            with open("books.json", "w") as bf:
                json.dump(books_data, bf, indent=4)
        except (IOError, TypeError) as e:
            print(f"Error while saving books data: {e}")
            
        try:
            with open("members.json", "w") as mf:
                json.dump(members_data, mf, indent=4)
        except (IOError, TypeError) as e:
            print(f"Error while saving members data: {e}")

    def load_data(self):
        try:
            with open("books.json", "r") as bf:
                data = json.load(bf)
                self.books = [Book.from_dict(x) for x in data] 
        except FileNotFoundError:
            print("Note: books.json not found. Starting with an empty book list.")
            self.books = []
        except json.JSONDecodeError:
            print("Error: books.json contains invalid JSON data. Starting with an empty book list.")
            self.books = []
        except Exception as e:
            print(f"An unexpected error occurred while loading books: {e}")
            self.books = []

        try:
            with open("members.json", "r") as mf:
                data = json.load(mf)
                self.members = [Member.from_dict(x) for x in data]
        except FileNotFoundError:
            print("Note: members.json not found. Starting with an empty member list.")
            self.members = []
        except json.JSONDecodeError:
            print("Error: members.json contains invalid JSON data. Starting with an empty member list.")
            self.members = []
        except Exception as e:
            print(f"An unexpected error occurred while loading members: {e}")
            self.members = []