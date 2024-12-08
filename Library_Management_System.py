class Library:
    def __init__(self,):
        self.book_list = []

    def add_book(self):
        while True:
            name = input("Enter the title of the book: ")
            author = input("Enter the name of author of the book: ")
            if not name or not author:
                print("The title or the author cannot be empty. Please try again.")
                continue
            if any(book['Title'].lower() == name.lower() for book in self.book_list):
                print("This book already exists in the library. You don't need to add it.")
            else:
                details = {"Title": name,
                           "Author": author}
                self.book_list.append(details)
                print("The book added successfully. Thank you.")
            choice = input("Do you want to add another book? (Yes/No): ").lower()
            if choice == "yes":
                continue
            elif choice == "no":
                print("Exiting the add book process.")
                break
            else:
                print("Please enter a valid choice.")
                return

    def view_avail_books(self):
        if not self.book_list:
            print("No books available.")
        else:
            for books in self.book_list:
                print(f"Title: {books['Title']}, Author : {books['Author']}")

    def borrow_book(self):
        borrow = input("Enter the name of the book you want to borrow: ")
        if not self.book_list:
            print("This book is not available.")
            return
        for books in self.book_list:
            if books['Title'].lower() == borrow.lower():
                self.book_list.remove(books)
                print("This book has been removed from the library and issued to you.")
                return
        print("This book is not available in the library.")

    def return_book(self):
        returning = input("Which book do you want to return? ")
        for books in self.book_list:
            if books['Title'].lower() == returning.lower():
                print("This book is already available in the library.")
                return
        author = input("Enter the name of the author: ")
        new_book = {"Title": returning, "Author": author}
        self.book_list.append(new_book)
        print("Book returned successfully.")

def greet():
    print('''
    =============================================
            LIBRARY MANAGEMENT SYSTEM
    =============================================
    ''')
def main():
    books = Library()
    while True:
        try:
            choice = int(input('''
            What do you want to do?
            1. Add books
            2. View available books
            3. Issue a book
            4. Return a book
            5. Exit
            '''))
            match choice:
                case 1:
                    books.add_book()
                case 2:
                    books.view_avail_books()
                case 3:
                    books.borrow_book()
                case 4:
                    books.return_book()
                case 5:
                    print("Thank you for using our library system. Bye.")
                    break
        except ValueError:
            print("The choice should be a number (1-5): ")
greet()
main()