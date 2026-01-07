from reader import Reader

class Librarian(Reader):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.readers_list = []

    def borrow_book(self, book):
        if len(self.books_list) > 5:
            print("You can't get more books.")
            return False
        if not book.book_borrowed(self.user_name):
            return False
        self.books_list.append(book)
        return True

    def add_new_reader(self, reader):
        self.readers_list.append(reader)

    def print_details(self):
        print(f"user id: {self.user_id}, user name: {self.user_name}.")
        for reader in self.readers_list:
            print(f"readr id: {reader.user_id}, reader name: {reader.user_name}")