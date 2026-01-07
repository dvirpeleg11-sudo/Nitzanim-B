from book import Book
from reader import Reader
from librarian import Librarian
from chief import ChiefLibrarian

# Books
b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("Dune", "Frank Herbert")

# Reader tests
r1 = Reader("101", "Dan")
r1.print_details()

r2 = Reader("102", "Maya")
r2.borrow_book(b1)
r2.print_details()

r3 = Reader("103", "Yosef")
r3.borrow_book(b2)
r3.borrow_book(b3)
r3.print_details()

# Librarian tests
l1 = Librarian("200", "Sarah")
l1.print_details()

l2 = Librarian("201", "David")
l2.add_new_reader(r1)
l2.add_new_reader(r2)
l2.print_details()

# Chief Librarian tests
c1 = ChiefLibrarian("300", "Noa")
c1.print_details()

c2 = ChiefLibrarian("301", "Adam")
c2.add_new_librarian(l1)
c2.add_new_librarian(l2)
c2.print_details()