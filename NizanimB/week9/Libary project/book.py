class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.status = "online"
        self.borrow_name = None

    def book_borrowed(self, user_name):
        if self.status != "borrowed":
            print("The book is already borrowed.")
            return False
        self.status = "borrowed"
        self.borrow_name = user_name
        return True

    def book_returned(self):
        if self.status == "online":
            print("The book was not borrowed from the first place.")
            return False
        self.status = "online"
        self.borrow_name = None
        return True

    def print_details(self):
        print(f"book name: {self.book_name}, book author: {self.author}, book status: {self.status}, book borrow name: {self.borrow_name}.")