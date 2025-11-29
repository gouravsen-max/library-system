# Author: Ayush Raj
# MCA Assignment 3

from library import Library

def main():
    print("====== Library Inventory System ======")

    lib = Library() 

    while True:
        print("\n---- Menu ----")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Report")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            print("\n-- Add New Book --")
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            
            if lib.add_book(title, author, isbn):
                print(f"Book '{title}' added successfully.")

        elif choice == "2":
            print("\n-- Register New Member --")
            name = input("Member Name: ").strip()
            mid = input("Member ID: ").strip()
            
            if lib.register_member(name, mid):
                print(f"Member '{name}' registered successfully.")

        elif choice == "3":
            print("\n-- Borrow Book --")
            mid = input("Enter Member ID: ").strip()
            isbn = input("Enter Book ISBN: ").strip()
            
            if lib.lend_book(mid, isbn):
                print("Book issued successfully.")
            else:
                print("Could not issue book (Check IDs and book availability).") 

        elif choice == "4":
            print("\n-- Return Book --")
            mid = input("Enter Member ID: ").strip()
            isbn = input("Enter Book ISBN: ").strip()
            
            if lib.take_return(mid, isbn):
                print("Book returned successfully.")
            else:
                print("Return failed (Check IDs and if the member borrowed this book).")

        elif choice == "5":
            print("\n------ Library Report ------")
            
            most = lib.most_borrowed_book()
            if most:
                print(f"Most Borrowed Book: {most.title} by {most.author} (Borrowed {most.borrow_count} times)")
            else:
                print("Most Borrowed Book: No books in the system or no books have been borrowed.")

            borrowed_count = lib.borrowed_books_count()
            print(f"Books Currently Borrowed: {borrowed_count}")
            print(f"Total Registered Members: {len(lib.members)}")
            print(f"Total Books in Inventory: {len(lib.books)}")


        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main() 