class Book:
    def _init_(self title author status):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def _init_(self):
        self.books = []

    def add_book(self book):
        self.books.append(book)

    def remove_book(self title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def get_book(self title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {book.status}")
            print()

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            status = input("Enter book status: ")
            book = Book(title author status)
            library.add_book(book)
            print("Book added successfully!")
            print()

        elif choice == 2:
            title = input("Enter book title to remove: ")
            if library.remove_book(title):
                print("Book removed successfully!")
            else:
                print("Book not found!")
            print()

        elif choice == 3:
            library.display_books()
            print()

        elif choice == 4:
            break

if _name_ == "_main_":
    main()
```