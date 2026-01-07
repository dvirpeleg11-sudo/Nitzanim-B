class Reader:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.books_list = []

    def borrow_book(self, book):
        if len(self.books_list) > 3:
            print("You can't get more books.")
            return False
        if not book.book_borrowed(self.user_name):
            return False
        self.books_list.append(book)
        return True

    def return_book(self, book):
        if not book in self.books_list:
            print("This book is not in the list.")
            return False

        self.books_list.remove(book)
        return True

    def print_details(self):
        print(f"user id: {self.user_id}, user name: {self.user_name}.")
        for book in self.books_list:
            print(f"book name: {book.book_name}, book author: {book.author}")