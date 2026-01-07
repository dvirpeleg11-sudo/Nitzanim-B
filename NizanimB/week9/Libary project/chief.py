from librarian import Librarian

class ChiefLibrarian(Librarian):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.librarians_list = []

    def borrow_book(self, book):
        if len(self.books_list) > 7:
            print("You can't get more books.")
            return False
        if not book.book_borrowed(self.user_name):
            return False
        self.books_list.append(book)
        return True

    def add_new_librarian(self, librarian):
        self.librarians_list.append(librarian)

    def print_details(self):
        print(f"user id: {self.user_id}, user name: {self.user_name}.")
        for librarian in self.librarians_list:
            print(f"librarian id: {librarian.user_id}, librarian name: {librarian.user_name}")

    # bonus
    def find_most_active_readers(self):

        librarians = self.librarians_list
        librarian = librarians[0]
        most_active_reader = librarian.readers_list[0]
        most_active_reader_names = [most_active_reader.user_name]
        most_active_reader_books = len(most_active_reader.book_list)

        for librarian in self.librarians_list:

            for reader in librarian.readers_list:
                reader_books = len(reader.books_list)

                if reader_books > most_active_reader_books:
                    most_active_reader = reader

                    while not most_active_reader_names:
                        removed_name = most_active_reader_names.pop()

                    most_active_reader_names.append(reader.user_name)
                    most_active_reader_books = reader_books

                elif reader_books == most_active_reader_books:

                    most_active_reader_names.append(reader.user_name)

        return most_active_reader_names